Name:		avogadrolibs
Version:	1.93.0
Release:	5
Summary:	An advanced molecular editor
License:	BSD
Group:		Sciences/Chemistry
Url:		http://www.openchemistry.org/projects/avogadro2/
Source0:	https://github.com/OpenChemistry/avogadrolibs/archive/%{version}/%{name}-%{version}.tar.gz
Source100:	avogadrolibs.rpmlintrc
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	spglib-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(MoleQueue)
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	mmtf-cpp-devel
BuildRequires:	msym-devel
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(msgpack)

%description
Avogadro is an advanced molecular editor designed for cross-platform use in
computational chemistry, molecular modeling, bioinformatics, materials science,
and related areas. It offers flexible rendering and a powerful plugin
architecture. The code in this repository is a rewrite of Avogadro with source
code split across a libraries repository and an application repository. Core
features and goals of the Avogadro project:

  * Open source distributed under the liberal 3-clause BSD license
  * Cross platform with nightly builds on Linux, Mac OS X and Windows
  * Intuitive interface designed to be useful to whole community
  * Fast and efficient embracing the latest technologies
  * Extensible, making extensive use of a plugin architecture
  * Flexible supporting a range of chemical data formats and packages

#----------------------------------------------------

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} >= %{version}-%{release}
Requires:	cmake(MoleQueue)
Requires:	pkgconfig(glew)
Requires:	spglib-devel
Provides:	avogadro2-devel = %{version}-%{release}

%description	devel
The %{name}-devel package contains header files for 
developing applications that use %{name}.

#----------------------------------------------------

%prep
%autosetup -p1

%build
%cmake_qt5 \
	-DOpenGL_GL_PREFERENCE=GLVND \
	-G Ninja

%ninja_build

%install
%ninja_install -C build

# Somehow lib64 becomes lib6464 here...
sed -i -e 's,6464,64,g;s,3232,32,g;s,x32x32,x32,g' %{buildroot}%{_libdir}/cmake/avogadrolibs/AvogadroLibsConfig.cmake

%files
%doc %{_docdir}/AvogadroLibs/
%{_libdir}/*.so.*
%{_libdir}/avogadro2/

%files devel
%{_includedir}/avogadro/
%{_libdir}/cmake/%{name}/
%{_libdir}/*.so
%{_libdir}/*.a
