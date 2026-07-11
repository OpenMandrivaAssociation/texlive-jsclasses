%global tl_name jsclasses
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Classes tailored for use with Japanese
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/latex/jsclasses
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jsclasses.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jsclasses.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jsclasses.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Classes jsarticle and jsbook are provided, together with packages
okumacro and okuverb. These classes are designed to work under ASCII
Corporation's Japanese TeX system ptex.

