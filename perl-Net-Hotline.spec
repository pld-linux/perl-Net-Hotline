%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Hotline
Summary:	Net::Hotline perl module
Summary(pl):	Modu³ perla Net::Hotline
Name:		perl-Net-Hotline
Version:	0.81
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Hotline - Perl libraries for the Hotline internet client.

%description -l pl
Net::Hotline - biblioteki perla dla intenetowego klienta Hotline.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Net/Hotline.pm
%{perl_sitelib}/Net/Hotline.pod
%{perl_sitelib}/Net/Hotline
%{perl_sitelib}/auto/Net/Hotline
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
