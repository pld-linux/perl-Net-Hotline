#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Hotline
Summary:	Net::Hotline perl module
Summary(pl):	Modu³ perla Net::Hotline
Name:		perl-Net-Hotline
Version:	0.83
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2efc774c5499f1e8919e140e274321c5
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Hotline - Perl libraries for the Hotline internet client.

%description -l pl
Net::Hotline - biblioteki perla dla internetowego klienta Hotline.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Net/Hotline.pm
%dir %{perl_vendorlib}/Net/Hotline
%{perl_vendorlib}/Net/Hotline/*.pm
%{perl_vendorlib}/Net/Hotline/Protocol
%{perl_vendorlib}/auto/Net/Hotline
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
