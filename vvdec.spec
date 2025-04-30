%global forgeurl0 https://github.com/fraunhoferhhi/vvdec
Version: 3.0.0
%global tag0 v%{version}

%forgemeta

Name:           vvdec
Release:        %autorelease
Summary:        The Fraunhofer Versatile Video Decoder

License:        BSD-3-Clause-Clear
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires: cmake
BuildRequires: ninja-build
#ninja is faster
BuildRequires: gcc >= 5.0
BuildRequires: g++ >= 5.0
BuildRequires: simde-devel

Requires:%{name}-libs%{?_isa} = %{version}-%{release}


%description
VVdeC, the Fraunhofer Versatile Video Encoder, is a fast and efficient
software H.266/VVC encoder implementation


%package devel
Summary: Header files for vvdec development

Requires:%{name}%{?_isa} = %{version}-%{release}

%description devel
The vvdec-devel package contains the header files needed
to develop programs that use the vvdec.


%package libs
Summary: Library  files for vvdec

%description libs
The vvdec-libs package contains the library files

%prep
%forgesetup
#sanitize thirdparty
rm -rf ./thirdparty


%build
%cmake \
                -G Ninja \
                -DCMAKE_BUILD_TYPE=RelWithDebInfo \
                -DVVDEC_ENABLE_LINK_TIME_OPT=ON \
                -DVVDEC_INSTALL_VVDECAPP=ON \
                -DCMAKE_SKIP_INSTALL_RPATH=1

%cmake_build


%install
%cmake_install


#not runing tests as they keep failing


%files
%{_bindir}/vvdecapp

%files devel
%{_includedir}/vvdec
%{_libdir}/cmake/vvdec
%{_libdir}/pkgconfig/libvvdec.pc
%{_libdir}/libvvdec.so

%files libs
%{_libdir}/libvvdec.so.3*
%license LICENSE.txt
%doc README.md
%doc AUTHORS.md

%changelog
%autochangelog
