%define upstream_name	 Time-Format
%define upstream_version 1.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl module for date and time formatting
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Time/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Time::Format provides a very easy way to format dates and times. The
formatting functions are tied to hash variables, so they can be used
inside strings as well as in ordinary expressions. The formatting
codes used are meant to be easy to remember, use, and read. They
follow a simple, consistent pattern. 
%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
