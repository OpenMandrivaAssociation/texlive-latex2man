Name:		texlive-latex2man
Version:	64477
Release:	1
Summary:	Translate LaTeX-based manual pages into Unix man format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/latex2man
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2man.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2man.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-latex2man.bin = %{EVRD}

%description
A tool to translate UNIX manual pages written with LaTeX into a
man-page format understood by the Unix man(1) command.
Alternatively HTML or TexInfo code can be produced. Output of
parts of the text may be supressed using the conditional text
feature.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/latex2man
%{_texmfdistdir}/scripts/latex2man
%{_texmfdistdir}/tex/latex/latex2man
%doc %{_infodir}/latex2man.info*
%doc %{_mandir}/man1/latex2man.1*
%doc %{_texmfdistdir}/doc/man/man1/latex2man.man1.pdf
%doc %{_texmfdistdir}/doc/support/latex2man

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
# generate relative link manually because it appears to trigger some
# weird bug that causes the link to be removed
%define dont_relink                        1
ln -sf ../share/texmf-dist/scripts/latex2man/latex2man latex2man
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdistdir}/doc/info/*.info %{buildroot}%{_infodir}
