# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/srcltx
# catalog-date 2006-12-07 15:13:33 +0100
# catalog-license pd
# catalog-version 1.6
Name:		texlive-srcltx
Version:	1.6
Release:	9
Summary:	Jump between DVI and TeX files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/srcltx
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srcltx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srcltx.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srcltx.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-2
+ Revision: 756163
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 719573
- texlive-srcltx
- texlive-srcltx
- texlive-srcltx
- texlive-srcltx

