%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	WrapI18N
Summary:	Text::WrapI18N - Line wrapping module with support for i18n
Name:		perl-Text-WrapI18N
Version:	0.06
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9f78b13b4c32c61e6aac5cefd75989dd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module intends to be a better Text::Wrap module. This module is
needed to support multibyte character encodings such as UTF-8, EUC-JP,
EUC-KR, GB2312, and Big5. This module also supports characters with
irregular widths, such as combining characters (which occupy zero
columns on terminal, like diacritical marks in UTF-8) and fullwidth
characters (which occupy two columns on terminal, like most of east
Asian characters). Also, minimal handling of languages which doesn't
use whitespaces between words (like Chinese and Japanese) is
supported.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Text/WrapI18N.pm
%{_mandir}/man3/*
