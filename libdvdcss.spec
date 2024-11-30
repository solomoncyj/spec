# adapted from https://code.videolan.org/videolan/libdvdcss/-/blob/master/libdvdcss.spec


Name:           libdvdcss
Version:        1.4.3
Release:        %autorelease
Summary:        Library for accessing DVDs like block devices with transparent decryption
Group:          System/Libraries
License:        GPL-2.0-or-later
URL:            https://code.videolan.org/videolan/libdvdcss
Source:         https://code.videolan.org/videolan/libdvdcss/-/archive/%{version}/libdvdcss-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

%description
libdvdcss is a simple library designed for accessing DVDs like a block device
without having to bother about the decryption. The important features are:
 * Portability: Currently supported platforms are GNU/Linux, FreeBSD, NetBSD,
   OpenBSD, Haiku, Mac OS X, Solaris, QNX, OS/2, and Windows 2000 or later.
 * Adaptability: Unlike most similar projects, libdvdcss does not require the
   region of your drive to be set and will try its best to read from the disc
   even in the case of a region mismatch.
 * Simplicity: A DVD player can be built around the libdvdcss API using no
   more than 4 or 5 library calls.

%package devel
Summary:        development files  for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
The %{name}-devel package contain development files

%prep
%autosetup -n %{name}-%{version}

%build
autoreconf --install --force --verbose
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}/usr/lib/debug/usr/lib64/libdvdcss.so.2.2.0-1.4.3-1.fc42.x86_64.debug

%files
%{_docdir}/libdvdcss
%license COPYING
%{_libdir}/libdvdcss.so.2*

%files devel
%{_includedir}/dvdcss
%{_libdir}/libdvdcss.so
%{_libdir}/libdvdcss.a
%{_libdir}/pkgconfig/libdvdcss.pc

%changelog
%autochangelog
