#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Hotline
Summary:	Net::Hotline - Perl libraries for the Hotline internet client
Summary(pl):	Net::Hotline - biblioteki Perla dla internetowego klienta Hotline
Name:		perl-Net-Hotline
Version:	0.83
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2efc774c5499f1e8919e140e274321c5
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Hotline::Client is a class implementing a Hotline Internet client
in Perl.  It was specifically developed to aid in the creation of Hotline
"bots," although it's suitable for most other tasks as well. Hotline is
an Internet client/server system that's sort of a cross between IRC and
a BBS.  See http://www.hotlinesw.com/ for more information.

%description -l pl
Net::Hotline::Client to klasa implementuj±ca internetowego klienta
Hotline w Perlu. Zosta³a zaprojektowana specjalnie, aby pomóc przy
tworzeniu "botów" dla Hotline, ale nadaje siê tak¿e dla wiêkszo¶ci
innych zadañ. Hotline to internetowy system klient-serwer bêd±cy
skrzy¿owaniem IRC-a i BBS-u. Wiêcej informacji mo¿na znale¼æ pod
adresem http://www.hotlinesw.com/ .

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
