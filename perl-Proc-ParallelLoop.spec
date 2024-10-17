%define	module	Proc-ParallelLoop

Name:		perl-%{module}
Version:	0.5
Release:	3

Summary:	Execute loops in parallel
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Proc/%{module}-%{version}.tgz

BuildRequires:	perl-devel
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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.5-1
+ Revision: 768281
- adapt to Mandriva Linux
- imported package perl-Proc-ParallelLoop


* Mon Apr 04 2011 jquelin <jquelin> 0.500.0-1.mga1
+ Revision: 80340
- imported package perl-Proc-ParallelLoop


* Mon Apr 04 2011 cpan2dist 0.5-1mga
- initial mageia release, generated with cpan2dist
