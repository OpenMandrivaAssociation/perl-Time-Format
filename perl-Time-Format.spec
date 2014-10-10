%define upstream_name	 Time-Format
%define upstream_version 1.12
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.12
Release:	2

Summary:	Perl module for date and time formatting
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Time/Time-Format-1.12.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Time::Format provides a very easy way to format dates and times. The
formatting functions are tied to hash variables, so they can be used
inside strings as well as in ordinary expressions. The formatting
codes used are meant to be easy to remember, use, and read. They
follow a simple, consistent pattern. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README Changes quickref.*
%{perl_vendorlib}/Time
%{_mandir}/man3/*

%changelog
* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.0
+ Revision: 410098
- rebuild using %%perl_convert_version

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdv2010.0
+ Revision: 387782
- update to new version 1.11

* Thu May 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-1mdv2009.0
+ Revision: 212937
- update to new version 1.09

* Wed May 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdv2009.0
+ Revision: 212230
- update to new version 1.08

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdv2009.0
+ Revision: 194957
- update to new version 1.07

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.02-1mdv2008.1
+ Revision: 136362
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Mar 17 2007 Anssi Hannula <anssi@mandriva.org> 1.02-1mdv2007.1
+ Revision: 145650
- intial package release for Mandriva


