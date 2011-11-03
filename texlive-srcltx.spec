# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/srcltx
# catalog-date 2006-12-07 15:13:33 +0100
# catalog-license pd
# catalog-version 1.6
Name:		texlive-srcltx
Version:	1.6
Release:	1
Summary:	Jump between DVI and TeX files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/srcltx
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srcltx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srcltx.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srcltx.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides a \special insertion into generated .dvi files
allowing one to jump from the .dvi file to the .tex source and
back again (given a .dvi viewer that supports this, such as Yap
or xdvi version 22.38 or later). This was originally written by
Aleksander Simonic, the author of the WinEdt shell.

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
%{_texmfdistdir}/tex/latex/srcltx/srcltx.sty
%{_texmfdistdir}/tex/latex/srcltx/srctex.sty
%doc %{_texmfdistdir}/doc/latex/srcltx/README
%doc %{_texmfdistdir}/doc/latex/srcltx/srcltx.pdf
#- source
%doc %{_texmfdistdir}/source/latex/srcltx/srcltx.dtx
%doc %{_texmfdistdir}/source/latex/srcltx/srcltx.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
