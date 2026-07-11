%global tl_name latex2man
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.30
Release:	%{tl_revision}.1
Summary:	Translate LaTeX-based manual pages into Unix man format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/latex2man
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2man.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2man.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(latex2man.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Latex2man is a tool to translate UNIX manual pages written with LaTeX
into the troff format understood by the UNIX man(1) command.
Alternatively HTML, Texinfo, or LaTeX code can be produced too. Output
of parts of the text may be suppressed using the conditional text
feature (for this, LaTeX generation may be used). There is a LaTeX
package (latex2man.sty) for writing the man page and a Perl script
(latex2man) that does the actual translation.

