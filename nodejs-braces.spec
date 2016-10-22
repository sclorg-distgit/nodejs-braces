%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name braces

Summary:       Fastest brace expansion for node.js
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.8.2
Release:       7%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/braces
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Fastest brace expansion for node.js, with the most complete 
support for the Bash 4.3 braces specification.

 - Complete support for the braces part of the Bash 4.3 Brace Expansion.
     Braces passes all of the relevant unit tests from the spec.
 - Expands comma-separated values: a/{b,c}/d => ['a/b/d', 'a/c/d']
 - Expands alphabetical or numerical ranges: {1..3} => ['1', '2', '3']
 - Very fast
 - Special characters can be used to generate interesting patterns.

%prep
%setup -q -n package

%nodejs_fixdep lazy-cache

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json utils.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%doc LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.8.2-7
- Use proper macro in -runtime dependency

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.8.2-6
- Use proper macro in -runtime dependency

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.8.2-5
- Use proper macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.8.2-4
- rebuilt

* Mon Jan 11 2016 Tomas Hrcka <thrcka@redhat.com> - 1.8.2-3
- Enable scl macros

* Thu Dec 17 2015 Troy Dawson <tdawson@redhat.com> - 1.8.2-2
- Fix dependencies

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 1.8.2-1
- Initial package