Name:		texlive-jsclasses
Version:	20190406
Release:	1
Summary:	Classes tailored for use with Japanese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jsclasses
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jsclasses.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jsclasses.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jsclasses.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Classes jsarticle and jsbook are provided, together with
packages okumacro, okuverb and morisawa. These classes are
designed to work under ASCII Corporation's Japanese TeX system
ptex.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/platex/jsclasses
%doc %{_texmfdistdir}/doc/platex/jsclasses
#- source
%doc %{_texmfdistdir}/source/platex/jsclasses

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
