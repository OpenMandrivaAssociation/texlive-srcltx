%global tl_name srcltx
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Jump between DVI and TeX files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/srcltx
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/srcltx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/srcltx.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/srcltx.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides a \special insertion into generated .dvi files allowing one to
jump from the .dvi file to the .tex source and back again (given a .dvi
viewer that supports this, such as Yap or xdvi version 22.38 or later).
This was originally written by Aleksander Simonic, the author of the
WinEdt shell.

