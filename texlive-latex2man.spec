Name:		texlive-latex2man
Version:	1.24
Release:	1
Summary:	Translate LaTeX-based manual pages into Unix man format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/latex2man
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2man.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2man.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-latex2man.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A tool to translate UNIX manual pages written with LaTeX into a
man-page format understood by the Unix man(1) command.
Alternatively HTML or TexInfo code can be produced. Output of
parts of the text may be supressed using the conditional text
feature.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/latex2man
%{_texmfdistdir}/scripts/latex2man/latex2man
%{_texmfdistdir}/tex/latex/latex2man/latex2man.cfg
%{_texmfdistdir}/tex/latex/latex2man/latex2man.sty
%doc %{_texmfdistdir}/doc/support/latex2man/CHANGES
%doc %{_texmfdistdir}/doc/support/latex2man/INSTALL
%doc %{_texmfdistdir}/doc/support/latex2man/Makefile
%doc %{_texmfdistdir}/doc/support/latex2man/README
%doc %{_texmfdistdir}/doc/support/latex2man/THIS-IS-VERSION-1.24
%doc %{_texmfdistdir}/doc/support/latex2man/latex2man-CHANGES.html
%doc %{_texmfdistdir}/doc/support/latex2man/latex2man.1
%doc %{_texmfdistdir}/doc/support/latex2man/latex2man.css
%doc %{_texmfdistdir}/doc/support/latex2man/latex2man.html
%doc %{_texmfdistdir}/doc/support/latex2man/latex2man.pdf
%doc %{_texmfdistdir}/doc/support/latex2man/latex2man.tex
%doc %{_texmfdistdir}/doc/support/latex2man/latex2man.texi
%doc %{_texmfdistdir}/doc/support/latex2man/latex2man.trans
%doc %{_texmfdistdir}/doc/support/latex2man/latex2man.txt
%doc %{_infodir}/latex2man.info*

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    # generate relative link manually because it appears to trigger some
    # weird bug that causes the link to be removed
    %define dont_relink			1
    ln -sf ../share/texmf-dist/scripts/latex2man/latex2man latex2man
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdir}/doc/info/*.info %{buildroot}%{_infodir}