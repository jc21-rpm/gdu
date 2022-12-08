%define debug_package %{nil}

%global gh_user dundee

Name:           gdu
Version:        5.20.0
Release:        1
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
* Thu Dec 8 2022 Jamie Curnow <jc@jc21.com> 5.20.0-1
- Initial spec
