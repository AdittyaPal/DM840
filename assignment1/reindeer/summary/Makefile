SHELL=/bin/bash
summary/all.tex: gen
	echo -n '\summaryGraph' >> summary/all.tex
	echo '{\texttt{g\_\{0\}}}{\summaryGraphFile{out/001_g_0_10300000}{\texttt{out/001\_g\_0\_10300000}}}{\summaryGraphFile{out/003_g_0_11310100}{\texttt{out/003\_g\_0\_11310100}}}' >> summary/all.tex
	echo -n '\summaryGraph' >> summary/all.tex
	echo '{\texttt{g\_\{1\}}}{\summaryGraphFile{out/005_g_1_10300000}{\texttt{out/005\_g\_1\_10300000}}}{\summaryGraphFile{out/007_g_1_11310100}{\texttt{out/007\_g\_1\_11310100}}}' >> summary/all.tex
	echo '\summaryRule{Jump}{\summaryRuleSpan{out/009_r_0_10300000}{out/009\_r\_0\_10300000}}{\summaryRuleSpan{out/011_r_0_11300100}{out/011\_r\_0\_11300100}}{}{out/012_r_0_constraints.tex}' >> summary/all.tex
	echo '\summaryRule{Move}{\summaryRuleSpan{out/014_r_1_10300000}{out/014\_r\_1\_10300000}}{\summaryRuleSpan{out/016_r_1_11300100}{out/016\_r\_1\_11300100}}{}{out/017_r_1_constraints.tex}' >> summary/all.tex
	echo '\summaryDGHyper{\texttt{dg\_0}}{out/297_dg_0_11100}{\texttt{out/297\_dg\_0\_11100}}' >> summary/all.tex
	echo '\summarySubsection{Solution 0}' >> summary/all.tex
	echo '\summarySubsubsection{Overall Data}' >> summary/all.tex
	echo '\input{out/299_f_0_0_listing.tex}' >> summary/all.tex
	echo '\summaryFlowFiltered{\texttt{dgFlow\_0, 0}}{out/301_dg_0_11100_f_0_0_filt}{\texttt{out/301\_dg\_0\_11100\_f\_0\_0\_filt}}' >> summary/all.tex
	echo '\summarySubsection{Solution 1}' >> summary/all.tex
	echo '\summarySubsubsection{Overall Data}' >> summary/all.tex
	echo '\input{out/302_f_0_1_listing.tex}' >> summary/all.tex
	echo '\summaryFlowFiltered{\texttt{dgFlow\_0, 1}}{out/304_dg_0_11100_f_0_1_filt}{\texttt{out/304\_dg\_0\_11100\_f\_0\_1\_filt}}' >> summary/all.tex
summary.pdf: summary/all.tex
	mod_post --mode compileSummary
include summary/MakefileImpl
include summary/MakefileDep
include summary/MakefileAllTarget
include summary/MakefileClean
