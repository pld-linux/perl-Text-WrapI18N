#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Text
%define		pnam	WrapI18N
Summary:	Text::WrapI18N - line wrapping module with support for i18n
Summary(pl.UTF-8):	Text::WrapI18N - moduł zawijający linie z obsługą międzynarodowości
Name:		perl-Text-WrapI18N
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0799c16a00926e6c18d400c2e2861d5f
URL:		http://search.cpan.org/dist/Text-WrapI18N/
%if %{with tests}
BuildRequires:	perl-Text-CharWidth >= 0.02
%endif
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

%description -l pl.UTF-8
Ten moduł ma być lepszą wersją Text::Wrap. Jest potrzebny do obsługi
wielobajtowych kodowań znaków, takich jak UTF-8, EUC-JP, EUC-KR,
GB2312 i Big5. Obsługuje także znaki o niestandardowej szerokości,
takie jak znaki łączone (zajmujące na terminalu zero kolumn, jak
znaczniki diakrytyczne w UTF-8) i znaki pełnej szerokości (zajmujące
na terminalu dwie kolumny, jak większość znaków wschodnioazjatyckich).
Jest także minimalna obsługa języków nie używających odstępów między
słowami (jak chiński czy japoński).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
