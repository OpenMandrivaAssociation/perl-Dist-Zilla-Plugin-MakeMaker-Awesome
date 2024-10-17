%define upstream_name    Dist-Zilla-Plugin-MakeMaker-Awesome
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A more awesome MakeMaker plugin for Dist::Zilla
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::File::InMemory)
BuildRequires:	perl(Dist::Zilla::Plugin::MakeMaker)
BuildRequires:	perl(Dist::Zilla::Role::BuildRunner)
BuildRequires:	perl(Dist::Zilla::Role::InstallTool)
BuildRequires:	perl(Dist::Zilla::Role::TestRunner)
BuildRequires:	perl(Dist::Zilla::Role::TextTemplate)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(MooseX::Types::Moose)
BuildRequires:	perl(namespace::autoclean)

BuildArch:	noarch

Obsoletes: perl-Dist-Zilla-Plugin-OverridableMakeMaker

%description
the Dist::Zilla manpage's Dist::Zilla::Plugin::MakeMaker plugin is limited,
if you want to stray from the marked path and do something that would
normally be done in a 'package MY' section or otherwise run custom code in
your _Makefile.PL_ you're out of luck.

This plugin is 100% compatable with the Dist::Zilla::Plugin::MakeMaker
manpage, but if you need something more complex you can just subclass it:

Then, in your _dist.ini_:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

