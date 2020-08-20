# Run tests in check section
# disable for bootstrapping
%bcond_with check
%global goipath golang-github-linuxdeepin-go-x11-client
%global with_debug 1

%if 0%{?with_debug}
%global debug_package   %{nil}
%endif
%gometa

%global provider        github
%global provider_tld    com
%global project         linuxdeepin
%global repo            go-x11-client

%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           golang-github-linuxdeepin-go-x11-client
Version:        0.6.0
Release:        0.10
Summary:        A X11 client Go bindings for Deepin Desktop Environment
License:        GPLv3
URL:            %{gourl}
Source0:        %{name}_%{version}.orig.tar.xz	
#BuildRequires:  compiler(go-compiler)
BuildRequires:  go-compilers-golang-compiler >= 1-35

%description
%{summary}.

%package devel
Summary:        %{summary}
BuildArch:      noarch
#BuildRequires:  golang(gopkg.in/check.v1)
#BuildRequires:  golang(golang.org/x/text/encoding/charmap)
#BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  testify-devel


%description devel
%{summary}.


%prep
%forgeautosetup

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
for file in $(find . -iname "*.go") ; do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done


%if %{with check}
%check
%gochecks
%endif

%files devel -f devel.file-list
%doc README
%license LICENSE

%changelog
* Tue Feb 26 2019 mosquito <sensor.wen@gmail.com> - 0-0.10.20190226git460ffe2
- Update to 460ffe2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git8411934
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 mosquito <sensor.wen@gmail.com> - 0-0.8.20181112git8411934
- Update to 8411934
- New X connect failed: WindowError
  https://github.com/linuxdeepin/developer-center/issues/590

* Sun Nov  4 2018 mosquito <sensor.wen@gmail.com> - 0-0.7.20181104git0354113
- Update to 0354113

* Sat Aug 25 2018 mosquito <sensor.wen@gmail.com> - 0-0.6.git71929bb
- Update to 71929bb

* Fri Jul 27 2018 mosquito <sensor.wen@gmail.com> - 0-0.5.git70dbb86
- Update to 70dbb86

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gita10a839
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gita10a839
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 14 2017 mosquito <sensor.wen@gmail.com> - 0-0.2.gita10a839
- Update to a10a839

* Sun Aug 27 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.git67aca0b
- Initial package build

