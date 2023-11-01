Name:           perl-Module-Install
Version:        1.19
Release:        2%{?dist}
Summary:        Standalone, extensible Perl module installer
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Module-Install/
Source0:        http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/Module-Install-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# XXX: BuildRequires:  perl(Archive::Zip) >= 1.37
# XXX: BuildRequires:  perl(Carp)
# XXX: BuildRequires:  perl(CPAN)
# XXX: BuildRequires:  perl(CPANPLUS::Backend)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::PPPort) >= 3.16
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(ExtUtils::MM_Unix)
# XXX: BuildRequires:  perl(ExtUtils::MM_Cygwin)
# XXX: BuildRequires:  perl(ExtUtils::MM_Win32)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
# XXX: BuildRequires:  perl(File::HomeDir) >= 1
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Remove) >= 1.42
BuildRequires:  perl(File::Spec) >= 3.28
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
# XXX: BuildRequires:  perl(JSON) >= 2.9
# XXX: BuildRequires:  perl(LWP::Simple) >= 6.00
# XXX: BuildRequires:  perl(Module::Build) >= 0.29
BuildRequires:  perl(Module::CoreList) >= 2.17
# XXX: BuildRequires:  perl(Module::ScanDeps) >= 1.09
# XXX: BuildRequires:  perl(Net::FTP)
# XXX: BuildRequires:  perl(PAR::Dist) >= 0.29
BuildRequires:  perl(Parse::CPAN::Meta) >= 1.4413
# XXX: BuildRequires:  perl(Socket)
BuildRequires:  perl(vars)
BuildRequires:  perl(YAML::Tiny) >= 1.38
# Tests only
BuildRequires:  perl(autodie)
BuildRequires:  perl(ExtUtils::MM)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
# Optional tests only
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::ExtraTests) >= 0.007
%endif
BuildRequires:  perl(utf8)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(Archive::Zip) >= 1.37
Requires:       perl(Carp)
Requires:       perl(CPAN)
# CPANPLUS is preferred over CPAN, but it's in a build cycle
# (perl-Module-Install → perl-CPANPLUS → perl-DBIx-Simple → perl-SQL-Abstract
# → perl-Module-Install), not necessary if all dependencies are retrived
# from an RPM repository, and upstream still considered as an option. Thus do
# not hard require the CPANPLUS.
Recommends:     perl(CPANPLUS::Backend)
Requires:       perl(Devel::PPPort) >= 3.16
Requires:       perl(ExtUtils::MakeMaker) >= 6.59
# Unused: Requires:       perl(ExtUtils::MM_Cygwin)
Requires:       perl(ExtUtils::MM_Unix)
# Unused: Requires:       perl(ExtUtils::MM_Win32)
# Unneeded: Requires:       perl(File::HomeDir) >= 1
Requires:       perl(File::Remove) >= 1.42
Requires:       perl(File::Spec) >= 3.28
Requires:       perl(File::Temp)
Requires:       perl(FileHandle)
Requires:       perl(FindBin)
# Optional: Requires:       perl(JSON) >= 2.9
# Optional: Requires:       perl(LWP::Simple) >= 6.00
Requires:       perl(Module::Build) >= 0.29
Requires:       perl(Module::CoreList) >= 2.17
Requires:       perl(Module::ScanDeps) >= 1.09
# Optional: Requires:       perl(Net::FTP)
# Optional: Requires:       perl(PAR::Dist) >= 0.29
Requires:       perl(Parse::CPAN::Meta) >= 1.4413
Requires:       perl(Socket)
Requires:       perl(YAML::Tiny) >= 1.38

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::PPPort\\)$
%global __requires_exclude %__requires_exclude|^perl\\(ExtUtils::MakeMaker\\)$
%global __requires_exclude %__requires_exclude|^perl\\(File::Remove\\)$
%global __requires_exclude %__requires_exclude|^perl\\(File::Spec\\)$
%global __requires_exclude %__requires_exclude|^perl\\(YAML::Tiny\\)$


%description
Module::Install is a package for writing installers for CPAN (or CPAN-like)
distributions that are clean, simple, minimalist, act in a strictly correct
manner with ExtUtils::MakeMaker, and will run on any Perl installation
version 5.005 or newer.

%prep
%setup -q -n Module-Install-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
rm -f %{buildroot}/blib/lib/auto/share/dist/Module-Install/dist_file.txt
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 22 2017 Petr Pisar <ppisar@redhat.com> - 1.19-1
- 1.19 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-2
- Perl 5.26 rebuild

* Wed Apr 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-1
- 1.18 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-1
- 1.17 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-10
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-9
- Perl 5.24 rebuild

* Mon Feb 22 2016 Petr Pisar <ppisar@redhat.com> - 1.16-8
- Recommend CPANPLUS instead of hard-requiring it

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-5
- Perl 5.22 re-rebuild of bootstrapped packages

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-4
- Perl 5.22 rebuild

* Mon May 04 2015 Petr Šabata <contyk@redhat.com> - 1.16-3
- Module::CoreList is actually required for build

* Mon May 04 2015 Petr Šabata <contyk@redhat.com> - 1.16-2
- Disable some optional tests to avoid a cycle

* Mon May 04 2015 Petr Šabata <contyk@redhat.com> - 1.16-1
- 1.16 bump

* Thu Apr 30 2015 Petr Šabata <contyk@redhat.com> - 1.15-1
- 1.15 bump
- Correct source URL
- Rewrite the dep list
- Drop the currently unused AUTOMATED_TESTING again

* Wed Oct 29 2014 Petr Pisar <ppisar@redhat.com> - 1.14-1
- 1.14 bump

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-2
- Perl 5.20 rebuild

* Tue Aug 19 2014 Petr Pisar <ppisar@redhat.com> - 1.10-1
- 1.10 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 01 2014 Petr Pisar <ppisar@redhat.com> - 1.06-6
- Do not build-require Test::MinimumVersion, xt tests are not performed
- Fix tests with Parse::CPAN::Meta >= 1.4413 (CPAN RT#93293)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Aug 01 2013 Petr Pisar <ppisar@redhat.com> - 1.06-4
- Perl 5.18 rebuild

* Wed Jan 30 2013 Paul Howarth <paul@city-fan.org> - 1.06-3
- Don't "unbundle" Module::Install as we end up build-requiring ourselves

* Tue Nov 20 2012 Petr Šabata <contyk@redhat.com> - 1.06-2
- Add missing deps
- Unbundle Module::Install
- Modernize the spec

* Fri Oct 05 2012 Petr Šabata <contyk@redhat.com> - 1.06-1
- 1.06 bump

* Fri Sep 14 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-4
- Update requires: perl(Carp), perl(CPAN), perl(CPANPLUS::Backend)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.04-2
- Perl 5.16 rebuild

* Thu Jan 12 2012 Iain Arnell <iarnell@gmail.com> 1.04-1
- update to latest upstream version

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.01-2
- Perl mass rebuild

* Sat May 14 2011 Iain Arnell <iarnell@gmail.com> 1.01-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Thu Mar 10 2011 Steven Pritchard <steve@kspei.com> 1.00-1
- Update to 1.00.
- Update build dependencies:
  + Archive::Tar >= 1.44
  + ExtUtils::Install >= 1.52
  + ExtUtils::ParseXS >= 2.19
  + JSON >= 2.14
  + LWP::UserAgent >= 5.812
  + Module::Build >= 0.29
  + Module::CoreList >= 2.17
  + Module::ScanDeps >= 0.89
- Update description (pulled from module).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.95-2
- 661697 rebuild for fixing problems with vendorach/lib

* Mon May 03 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.95-1
- Mass rebuild with perl-5.12.0 & update

* Thu Feb 25 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.91-4
- change to DESTDIR
- add README
- dist_file.txt wasn't packaged -> removed, it's needed only for test of build

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.91-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 14 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.91-1
- update to 0.91
- add br on Parse::CPAN::Meta: 1.39

* Sat May 23 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.90-1
- update to 0.90 
- add br on JSON, Test::Harness (3.13)
- update br on YAML::Tiny (1.38)

* Mon May 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.87-1
- update to 0.87

* Sun Apr 26 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.85-1
- update to 0.85
- add BR on File::Spec

* Thu Apr 09 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.82-1
- update to 0.82

* Sun Mar 22 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.80-1
- update to 0.80 
- remove 03_autoinstall.t swizzle (now self-skipped; see RT29448)

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.79-1
- update to 0.79

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 04 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.77-1
- update to 0.77

* Wed Jun 04 2008 Steven Pritchard <steve@kspei.com> 0.75-1
- Update to 0.75.

* Sat May 31 2008 Steven Pritchard <steve@kspei.com> 0.74-1
- Update to 0.74.
- Update versioned dependencies for File::Remove, Module::ScanDeps,
  PAR::Dist, and YAML::Tiny.
- BR Test::CPAN::Meta.

* Fri May 16 2008 Steven Pritchard <steve@kspei.com> 0.73-1
- Update to 0.73.
- BR File::Remove.
- Drop zero-length README.

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.68-3
- disable broken test (upstream bug present)
- add Test::MinimumVersion as BR

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.68-2
- rebuild for new perl

* Mon Jan 28 2008 Steven Pritchard <steve@kspei.com> 0.68-1
- Update to 0.68.
- Explicitly require Archive::Tar and ExtUtils::ParseXS.

* Sun Dec 30 2007 Ralf Corsépius <rc040203@freenet.de> - 0.67-2
- BR: perl(Test::More), perl(CPAN) (BZ 419631).
- Remove TEST_POD (Unused).
- Add AUTOMATED_TESTING.
- BR: perl(Test::Pod) for AUTOMATED_TESTING.
- Adjust License-tag.

* Fri May 18 2007 Steven Pritchard <steve@kspei.com> 0.67-1
- Update to 0.67.
- BR Archive::Tar, ExtUtils::ParseXS, and YAML::Tiny.
- Add a couple more docs.

* Tue Mar 13 2007 Steven Pritchard <steve@kspei.com> 0.65-1
- Update to 0.65.
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Sun Sep 17 2006 Steven Pritchard <steve@kspei.com> 0.64-2
- Rebuild.

* Fri Aug 25 2006 Steven Pritchard <steve@kspei.com> 0.64-1
- Update to 0.64.
- Fix find option order.

* Thu Jun 08 2006 Steven Pritchard <steve@kspei.com> 0.63-1
- Update to 0.63.

* Mon May 08 2006 Steven Pritchard <steve@kspei.com> 0.62-2
- Fix Source0 URL.

* Sat May 06 2006 Steven Pritchard <steve@kspei.com> 0.62-1
- Update to 0.62.
- Drop executable bit from everything in vendor_perl to make rpmlint happy.

* Thu Mar 23 2006 Steven Pritchard <steve@kspei.com> 0.61-1
- Specfile autogenerated by cpanspec 1.63.
- Drop explicit BR: perl.
- Turn on TEST_POD.
