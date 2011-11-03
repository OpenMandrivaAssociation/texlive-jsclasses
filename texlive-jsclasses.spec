# revision 18430
# category Package
# catalog-ctan /macros/latex/contrib/jsclasses
# catalog-date 2007-12-08 14:15:18 +0100
# catalog-license bsd
# catalog-version undef
Name:		texlive-jsclasses
Version:	20071208
Release:	1
Summary:	Classes tailored for use with Japanese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jsclasses
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jsclasses.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jsclasses.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Classes jsarticle and jsbook are provided, together with
packages okumacro, okuverb and morisawa. These classes are
designed to work under ASCII Corporation's Japanese TeX system
ptex.

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
%{_texmfdistdir}/tex/platex/jsclasses/jsarticle.cls
%{_texmfdistdir}/tex/platex/jsclasses/jsbook.cls
%{_texmfdistdir}/tex/platex/jsclasses/jspf.cls
%{_texmfdistdir}/tex/platex/jsclasses/jsverb.sty
%{_texmfdistdir}/tex/platex/jsclasses/kiyou.cls
%{_texmfdistdir}/tex/platex/jsclasses/minijs.sty
%{_texmfdistdir}/tex/platex/jsclasses/morisawa.sty
%{_texmfdistdir}/tex/platex/jsclasses/okumacro.sty
%{_texmfdistdir}/tex/platex/jsclasses/okuverb.sty
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
