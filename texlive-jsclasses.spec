# revision 30855
# category Package
# catalog-ctan /macros/latex/contrib/jsclasses
# catalog-date 2013-05-27 13:53:30 +0200
# catalog-license bsd
# catalog-version undef
Name:		texlive-jsclasses
Version:	20130527
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
%{_texmfdistdir}/tex/platex/jsclasses/jsarticle.cls
%{_texmfdistdir}/tex/platex/jsclasses/jsbook.cls
%{_texmfdistdir}/tex/platex/jsclasses/jspf.cls
%{_texmfdistdir}/tex/platex/jsclasses/jsverb.sty
%{_texmfdistdir}/tex/platex/jsclasses/kiyou.cls
%{_texmfdistdir}/tex/platex/jsclasses/minijs.sty
%{_texmfdistdir}/tex/platex/jsclasses/morisawa.sty
%{_texmfdistdir}/tex/platex/jsclasses/okumacro.sty
%{_texmfdistdir}/tex/platex/jsclasses/okuverb.sty
%doc %{_texmfdistdir}/doc/platex/jsclasses/README
%doc %{_texmfdistdir}/doc/platex/jsclasses/jsclasses.pdf
%doc %{_texmfdistdir}/doc/platex/jsclasses/jsverb.pdf
%doc %{_texmfdistdir}/doc/platex/jsclasses/morisawa.pdf
%doc %{_texmfdistdir}/doc/platex/jsclasses/okumacro.pdf
%doc %{_texmfdistdir}/doc/platex/jsclasses/okuverb.pdf
#- source
%doc %{_texmfdistdir}/source/platex/jsclasses/jsclasses.dtx
%doc %{_texmfdistdir}/source/platex/jsclasses/jsclasses.ins
%doc %{_texmfdistdir}/source/platex/jsclasses/jsverb.dtx
%doc %{_texmfdistdir}/source/platex/jsclasses/jsverb.ins
%doc %{_texmfdistdir}/source/platex/jsclasses/morisawa.dtx
%doc %{_texmfdistdir}/source/platex/jsclasses/morisawa.ins
%doc %{_texmfdistdir}/source/platex/jsclasses/okumacro.dtx
%doc %{_texmfdistdir}/source/platex/jsclasses/okumacro.ins
%doc %{_texmfdistdir}/source/platex/jsclasses/okuverb.dtx
%doc %{_texmfdistdir}/source/platex/jsclasses/okuverb.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
