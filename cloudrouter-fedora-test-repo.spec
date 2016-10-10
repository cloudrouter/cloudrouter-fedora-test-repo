%define cr_display_name CloudRouter
%define cr_name cloudrouter
%define cr_version 4

%define base_display_name Fedora 24
%define base_name fedora

Summary:	%{cr_display_name} test repository files for %{base_display_name}
Name:		%{cr_name}-%{base_name}-test-repo
Version:	%{cr_version}
Release:	1
License:	AGPLv3
Group:		System Environment/Base
Source0:	%{cr_name}-test.repo
BuildArch:	noarch
Provides:	cloudrouter-test-repo

%description
%{cr_display_name} test repository files for %{base_display_name}.

%prep
%setup -q  -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT

# Create dirs
install -dm 755 \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# Install repo
install -pm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*

%changelog
* Mon Oct 10 2016 John Siegrist <john@complects.com> - 4-1
- Initial commit of test-repo spec starting with CRv4.
