%define artipie_jar artipie-v%{getenv:GITHUB_REF_NAME}-jar-with-dependencies.jar
%define rpm_dir     packaging/rpm

Name:      artipie
Version:   %{getenv:GITHUB_REF_NAME}
Release:   1
BuildArch: noarch
Summary:   Package repository and cache server
License:   MIT
URL:       https://www.artipie.com
Group:     Development/Tools/Other

%description
HTTP server supporting many package repository formats
(NPM, PyPi, Docker, RubyGems, etc),
some with caching proxy ability,
each running on its own path or port.

%install
mkdir -p                      %{buildroot}%{_sysconfdir}/artipie/repos/
cp %{rpm_dir}/artipie.yml     %{buildroot}%{_sysconfdir}/artipie.yml

mkdir -p                      %{buildroot}%{_sysconfdir}/systemd/system/
cp %{rpm_dir}/artipie.service %{buildroot}%{_sysconfdir}/systemd/system/artipie.service

mkdir -p                      %{buildroot}/opt/artipie/
cp %{artipie_jar}             %{buildroot}/opt/artipie/artipie.jar

mkdir -p                      %{buildroot}%{_var}/cache/artipie/
mkdir -p                      %{buildroot}%{_var}/artipie/repos/

%files
%defattr(644, artipie, artipie, 755)

%dir %{_sysconfdir}/artipie
%{_sysconfdir}/artipie.yml
%{_sysconfdir}/artipie/repos/

%{_sysconfdir}/systemd/system/artipie.service

%dir /opt/artipie
/opt/artipie/artipie.jar

%{_var}/cache/artipie/
%{_var}/artipie/repos/

%changelog
* Tue Jan 17 2023 Ilya Vassilevsky <vassilevsky@gmail.com> - 0.28.0-1
- First version of artipie package
