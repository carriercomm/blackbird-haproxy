%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define name blackbird-haproxy
%define version 0.1.0
%define unmangled_version %{version}
%define release 1%{dist}
%define include_dir /etc/blackbird/conf.d
%define plugins_dir /opt/blackbird/plugins

Summary: Get stats of HAProxy for blackbird by using "show stats".
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: WTFPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: ARASHI, Jumpei <jumpei.arashi@arashike.com>
Packager: ARASHI, Jumpei <jumpei.arashi@arashike.com>
Requires: blackbird
Url: https://github.com/Vagrants/blackbird-haproxy
BuildRequires:  python-setuptools

%description
UNKNOWN

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

install -dm 0755 $RPM_BUILD_ROOT%{include_dir}
install -dm 0755 $RPM_BUILD_ROOT%{plugins_dir}
install -p -m 0644 scripts/haproxy.cfg $RPM_BUILD_ROOT%{include_dir}/haproxy.cfg
install -p -m 0644 haproxy.py $RPM_BUILD_ROOT%{plugins_dir}/haproxy.py

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%dir %{include_dir}
%config(noreplace) %{include_dir}/haproxy.cfg
%dir %{plugins_dir}
%{plugins_dir}/haproxy.*

%changelog
* Mon Jan 06 2014 ARASHI, Jumpei <jumpei.arashi@arashike.com> - 0.1.0-1
- Initial package
