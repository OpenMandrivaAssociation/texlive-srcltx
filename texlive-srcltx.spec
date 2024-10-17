Name:		texlive-srcltx
Version:	15878
Release:	2
Summary:	Jump between DVI and TeX files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/srcltx
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srcltx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srcltx.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srcltx.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a \special insertion into generated .dvi files
allowing one to jump from the .dvi file to the .tex source and
back again (given a .dvi viewer that supports this, such as Yap
or xdvi version 22.38 or later). This was originally written by
Aleksander Simonic, the author of the WinEdt shell.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/srcltx/srcltx.sty
%{_texmfdistdir}/tex/latex/srcltx/srctex.sty
%doc %{_texmfdistdir}/doc/latex/srcltx/README
%doc %{_texmfdistdir}/doc/latex/srcltx/srcltx.pdf
#- source
%doc %{_texmfdistdir}/source/latex/srcltx/srcltx.dtx
%doc %{_texmfdistdir}/source/latex/srcltx/srcltx.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
