%define	module	Proc-ParallelLoop

Name:		perl-%{module}
Version:	0.5
Release:	1

Summary:	Execute loops in parallel
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Proc/%{module}-%{version}.tgz
BuildArch:	noarch

%description
This module provides a way to easily write for loops and foreach loops that
run with a controlled degree of parallelism. One very nice feature is that
bufferring is used when necessary such that the output from STDERR and
STDOUT looks exactly as if it was produced by running your subroutine on
each parameter in plain old sequential fashion. Return status from each
loop iteration is also preserved.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*
