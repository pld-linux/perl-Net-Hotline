%include	/usr/lib/rpm/macros.perl
Summary:	Net-Hotline perl module
Summary(pl):	Modu³ perla Net-Hotline
Name:		perl-Net-Hotline
Version:	0.78
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Hotline-%{version}.tar.gz
Patch:		perl-Net-Hotline-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net-Hotline - Perl libraries for the Hotline internet client.

%description -l pl
Net-Hotline - biblioteki perla dla intenetowego klienta Hotline.

%prep
%setup -q -n Net-Hotline-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}

make install DESTDIR=$RPM_BUILD_ROOT

install Examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Net/Hotline
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,TODO}.gz

%{perl_sitelib}/Net/Hotline.pm
%{perl_sitelib}/Net/Hotline
%{perl_sitelib}/auto/Net/Hotline
%{perl_sitearch}/auto/Net/Hotline

%{_mandir}/man3/*

/usr/src/examples/%{name}
