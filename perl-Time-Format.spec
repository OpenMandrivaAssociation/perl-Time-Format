
%define module	Time-Format
%define name	perl-%{module}
%define version	1.02
%define rel	1

Summary:	Perl module for date and time formatting
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Time/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Time::Format provides a very easy way to format dates and times. The
formatting functions are tied to hash variables, so they can be used
inside strings as well as in ordinary expressions. The formatting
codes used are meant to be easy to remember, use, and read. They
follow a simple, consistent pattern. 
%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes quickref.*
%{perl_vendorlib}/Time
%{_mandir}/man3/*


