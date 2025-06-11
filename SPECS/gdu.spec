%define debug_package %{nil}

%global gh_user dundee

Name:           gdu
Version:        5.31.0
Release:        1%{?dist}
Summary:        Fast disk usage analyzer with console interface written in Go
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  golang

%description
Pretty fast disk usage analyzer written in Go.

Gdu is intended primarily for SSD disks where it can fully utilize parallel
processing. However HDDs work as well, but the performance gain is not so huge.

%prep
%setup -q -n %{name}-%{version}

%build
make build-static

%install
install -Dm0755 dist/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc LICENSE.md

%changelog
* Thu Jun 12 2025 Jamie Curnow <jc@jc21.com> 5.31.0-1
- v5.31.0

* Tue Jun 18 2024 Jamie Curnow <jc@jc21.com> 5.29.0-1
- v5.29.0

* Mon Apr 22 2024 Jamie Curnow <jc@jc21.com> 5.28.0-1
- v5.28.0

* Mon Feb 19 2024 Jamie Curnow <jc@jc21.com> 5.27.0-1
- v5.27.0

* Tue Feb 13 2024 Jamie Curnow <jc@jc21.com> 5.26.0-1
- v5.26.0

* Wed Jun 6 2023 Jamie Curnow <jc@jc21.com> 5.25.0-1
- v5.25.0

* Tue Jun 6 2023 Jamie Curnow <jc@jc21.com> 5.24.0-1
- v5.24.0

* Tue Feb 7 2023 Jamie Curnow <jc@jc21.com> 5.22.0-1
- v5.22.0

* Fri Feb 3 2023 Jamie Curnow <jc@jc21.com> 5.21.1-1
- v5.21.1

* Thu Jan 5 2023 Jamie Curnow <jc@jc21.com> 5.21.0-1
- v5.21.0

* Thu Dec 8 2022 Jamie Curnow <jc@jc21.com> 5.20.0-1
- Initial spec

