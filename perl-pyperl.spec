#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Python
%define		pnam	pyperl
Summary:	Encapuslate python objects
Name:		perl-Python-pyperl
Version:	1.0
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	6e48c2c889bf55c2656e6ed4589854bf
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	python-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Encapuslate python objects.

%prep
%setup -q -n %{pnam}-%{version}

%build
cd Python-Object
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C Python-Object install \
	DESTDIR=$RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Python
%{perl_vendorarch}/Python.pm
%dir %{perl_vendorarch}/auto/Python
%dir %{perl_vendorarch}/auto/Python/Object
%attr(755,root,root) %{perl_vendorarch}/auto/Python/Object/*.so
%{_mandir}/man3/*

%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/*.so
