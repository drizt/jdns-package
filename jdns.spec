Name:           jdns
Version:        2.0.0
Release:        3%{?dist}
Summary:        A simple DNS queries library

License:        MIT
URL:            http://delta.affinix.com/jdns/
Source0:        http://delta.affinix.com/download/%{name}-%{version}.tar.bz2

BuildRequires:  qt4-devel
BuildRequires:  cmake
Obsoletes:      qjdns < 2.0.0
Obsoletes:      qjdns-devel < 2.0.0

%description
JDNS is a simple DNS implementation that can perform normal DNS
queries of any record type (notably SRV), as well as Multicast DNS
queries and advertising. Multicast support is based on Jeremie
Miller's "mdnsd" implementation.

For maximum flexibility, JDNS is written in C with no direct
dependencies, and is licensed under the MIT license. Your application
must supply functionality to JDNS, such as UDP sending/receiving, via
callbacks.

%package -n     qjdns
Summary:        Qt-wrapper for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n qjdns
JDNS is a simple DNS implementation that can perform normal DNS
queries of any record type (notably SRV), as well as Multicast DNS
queries and advertising. Multicast support is based on Jeremie
Miller's "mdnsd" implementation.

For maximum flexibility, JDNS is written in C with no direct
dependencies, and is licensed under the MIT license. Your application
must supply functionality to JDNS, such as UDP sending/receiving, via
callbacks.

For Qt users there is a wrapper available called QJDns and a very
high-level wrapper called QJDnsShared (under its original name
JDnsShared).

Qt-based command-line tool called ‘jdns’ that can be used to test
functionality.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
JDNS is a simple DNS implementation that can perform normal DNS
queries of any record type (notably SRV), as well as Multicast DNS
queries and advertising. Multicast support is based on Jeremie
Miller's "mdnsd" implementation.

For maximum flexibility, JDNS is written in C with no direct
dependencies, and is licensed under the MIT license. Your application
must supply functionality to JDNS, such as UDP sending/receiving, via
callbacks.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} -DQT4_BUILD=ON ..
make %{?_smp_mflags}
popd

%install
%make_install -C %{_target_platform}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%check
export PKG_CONFIG_PATH=%{buildroot}%{_qt4_libdir}/pkgconfig:
# The pkg-config versions should match the soversions.
test "$(pkg-config --modversion jdns)" = %{version}
test "$(pkg-config --modversion qjdns)" = %{version}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post -n qjdns -p /sbin/ldconfig
%postun -n qjdns -p /sbin/ldconfig


%files
%doc COPYING README.md
%{_libdir}/libjdns.so.*

%files -n qjdns
%{_bindir}/jdns
%{_libdir}/libqjdns.so.*

%files devel
%{_includedir}/jdns/
%{_libdir}/libjdns.so
%{_libdir}/libqjdns.so
%{_libdir}/cmake/jdns/
%{_libdir}/cmake/qjdns/
%{_libdir}/pkgconfig/jdns.pc
%{_libdir}/pkgconfig/qjdns.pc


%changelog
* Wed Apr  9 2014 Ivan Romanov <drizt@land.ru> - 2.0.0-3
- removed jdns binary from jdns package
- dropped reduntant dependencies
- use only %%{buildroot}
- merged jdns-bin with qjdns subpackage

* Fri Apr  4 2014 Ivan Romanov <drizt@land.ru> - 2.0.0-2
- dropped __requires_exclude_from hach
- dropped removing buildroot before installing

* Thu Apr  3 2014 Ivan Romanov <drizt@land.ru> - 2.0.0-1
- Initial version of package
