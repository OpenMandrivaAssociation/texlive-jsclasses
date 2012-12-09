# revision 18430
# category Package
# catalog-ctan /macros/latex/contrib/jsclasses
# catalog-date 2007-12-08 14:15:18 +0100
# catalog-license bsd
# catalog-version undef
Name:		texlive-jsclasses
Version:	20071208
Release:	2
Summary:	Classes tailored for use with Japanese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jsclasses
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jsclasses.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jsclasses.source.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20071208-2
+ Revision: 752933
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20071208-1
+ Revision: 718757
- texlive-jsclasses
- texlive-jsclasses
- texlive-jsclasses
- texlive-jsclasses

