Name: {{{ git_dir_name }}}
Version: {{{ git_dir_version lead=3.2 }}}
Release: 1%{?dist}
Summary: Control Redragon gaming mice from Linux, BSD and Haiku

License: GPL v3
URL:     https://github.com/dokutan/mouse_m908
BuildRequires: gcc-c++ libusb-devel make
Requires: libusb
ExclusiveArch: x86_64
Source: {{{ git_dir_pack }}}

%description
Control Redragon gaming mice from Linux, BSD and Haiku

%prep
{{{ git_dir_setup_macro }}}

%build
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_docdir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}/udev/rules.d

make \
     PREFIX=%{buildroot} \
     BIN_DIR=%{buildroot}/%{_bindir} \
     ETC_DIR=%{buildroot}/%{_sysconfdir} \
     DOC_DIR=%{buildroot}%{_docdir} \
     MAN_DIR=%{buildroot}%{_mandir}/man1 install


%clean
rm -rf %{buildroot}

%pre

%post

%files
%{_bindir}/%{name}
%{_docdir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_sysconfdir}/udev/rules.d/%{name}.rules

%changelog
{{{ git_dir_changelog }}}
