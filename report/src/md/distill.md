# Continuous Distillation : Experiment 4

## Objective

The objective is to study the process of continuous distillation in a sieve
plate column, for the separation of a water-ethanol mixture. The tray efficiency
for the column, mass and energy balances, and heat loss should also be
determined.

## Apparatus Required

*Equipment required:* Distillation column made of glass with perforated plates,
specific gravity bottle, specific gravity balance, Abbe refractometer,
laboratory droppers, laboratory glassware.

The mixture to be separated is ethanol-water. The actual number of plates in the
distillation column is $12$. Metering pumps have been used for the feed and the
reflux.

## Theory

Doctor Strange planned the ENDGAME all along.

### Assumptions

In order to plot the locus of all passing streams in the rectifying section as a
straight line of the form $y = mx + c$, the total molar flow rates $L$ and $V$
cannot vary from stage to stage. The following are the *McCabe-Thiele
assumptions* @seader2016separation, @gorak2014distillation.

1. The mixture is binary.
2. The column operates in the steady-state condition.
3.  The feed stream is mixed with the feed stage fluids prior to separation.
4. Each stage reaches equilibrium.
5. The two components have equal and constant molar enthalpies of vaporization
   (latent heats).
6. Component sensible-enthalpy changes ($C_p \Delta T$) and heat of mixing are
   negligible compared to latent heat changes.
7. The column is well insulated so that heat loss is negligible.
8. The pressure is uniform throughout the column (no pressure drop).

The assumptions above lead to the condition of *constant molar overflow* in the
rectifying section. Constant molar overflow refers to a molar liquid flow rate
that remains constant as the liquid flows over each weir, from one stage to the
next.

### External Reflux Ratio

The liquid entering the top stage is the external reflux rate, $L_0$, and its
ratio to the distillate rate, $L_0/D$, is the reflux ratio, $R$. Because of the
assumption of constant molar overflow, $R$ is a constant in the rectifying
section @seader2016separation, @smith2012distillation:

$$ R = \frac{L}{D} $$

### Rectifying Section

![Rectifying Section](img/1533580926428.png)

A material balance for the light key over the envelope shown in the figure for
the total condenser and stages $1$ to $n$ is as follows, where $y$ and $x$ refer
to vapor and liquid mole fractions, respectively, for the light key:

$$ V_{n+l} y_{n+l} = L_n x_n + D x_D $$

### Feed Conditions

blah blah

| **Feed condition** | **f** | **q** | **q Calculation** |
| ---------------------- | ----------- | ---------- | ------------------------------------------------------------ |
| Subcooled liquid | $f < 0$ | $q > 1$ | $q = [c_{P,L} (T_{bp} - T_F ) + \Delta H_{vap} ]/ \Delta H_{vap}$ |
| Liquid at bubble point | $0$ | $1$ | $q = \Delta H_{vap} / \Delta H_{vap} = 1$ |
| Partially vaporized | $0 < f < 1$ | $1< q < 0$ | $q = [(1 - f) \Delta H_{vap} ] / \Delta H_{vap} $ |
| Vapor at dew point | $1$ | $0$ | $q = 0$ |
| Superheated vapor | $f > 1$ | $q < 0$ | $q = - [c_{P,V} (T_F - T_{dp} )] / \Delta H_{vap} $ |

caption: Possible Feed Conditions and Corresponding $q$ Values
@gorak2014distillation

## Procedure 

1. The flow rate through the condenser was set at $2.5 L/min$.
2. The calibration curve for refractive index with alcohol percent was obtained.
   The calibration curve for specific gravity was also calculated.
3. The feed composition was determined and the reboiler was filled with it.
4. The reboiler was started and cooling water began circulation in the
   condenser.
5. For operating the column using total reflux, the entire distillate was
   returned to the column, and no secondary feed was provided. Secondary feed
   was provided only for the partial reflux cases.
6. The minimum reflux ratio for the feed conditions was determined, assuming 85
   mole purity of the distillate.
7. The column was operated under a reflux ratio higher than minimum reflux
   ratio, and samples were obtained at the steady states.
8. A sample from the bottoms was collected every $10$ minutes. The refractive
   index was measured using an Abbe refractometer. The specific gravity of the
   distillate was measured.
9. All the flow rates (distillate, reflux, feed, cooling water) and temperature
   (bottom, distillate, condenser inlet and outlet) were measured. The power
   (kwh) point input to boiler was also measured.
10. After the total reflux condition was achieved, a secondary feed was used to
    operate the column using a reflux ratio between $3$ to $4$.
11. The flow rates of the distillate and bottoms were adjusted so that the
    overall mass balance adjusted for the desired reflux ratio.
12. The total distillate and bottoms were collected and measured to verify the
    overall mass balance.
13. The refractive index of the total bottoms and the specific gravity of the
    distillate was measured to get an indication of the degree of purification
    for a fixed reflux ratio.
    
    The overall electricity consumption was also measured for the entire process.

## Line Diagram 

Welcome to the 20th century. We have pictures now.

##  Tables and Graphs

<!-- % Table generated by Excel2LaTeX from sheet 'Equilibrium Curve Data' -->

\begin{table}[htbp]
  \centering
  \caption{Calibration Curve Data}
    \begin{tabular}{ccccccccc}
    \multicolumn{9}{c}{} \\
    \multicolumn{2}{c}{\textcolor[rgb]{ .122,  .286,  .49}{\textbf{Volume (ml)}}} & \multicolumn{2}{c}{\textcolor[rgb]{ .122,  .286,  .49}{\textbf{Moles}}} & \multicolumn{2}{c}{\textcolor[rgb]{ .122,  .286,  .49}{\textbf{Mole Fraction}}} & \multicolumn{1}{p{5.315em}}{\textcolor[rgb]{ .122,  .286,  .49}{\textbf{Refraction Index}}} & \multicolumn{1}{p{7.375em}}{\textcolor[rgb]{ .122,  .286,  .49}{\textbf{Mass of Bottle (+Sample) (mg)}}} & \multicolumn{1}{p{4.19em}}{\textcolor[rgb]{ .122,  .286,  .49}{\textbf{Specific Gravity}}} \\
    \midrule
    \multicolumn{1}{l}{\textcolor[rgb]{ .122,  .286,  .49}{\textbf{Ethanol}}} & \multicolumn{1}{l}{\textcolor[rgb]{ .122,  .286,  .49}{\textbf{Water}}} & \multicolumn{1}{l}{\textcolor[rgb]{ .122,  .286,  .49}{\textbf{Ethanol}}} & \multicolumn{1}{l}{\textcolor[rgb]{ .122,  .286,  .49}{\textbf{Water}}} & \multicolumn{1}{l}{\textcolor[rgb]{ .122,  .286,  .49}{\textbf{Ethanol}}} & \multicolumn{1}{l}{\textcolor[rgb]{ .122,  .286,  .49}{\textbf{Water}}} &       &       &  \\
\cmidrule{1-6}    0     & 18    & 0     & 1     & 0     & 1     & 1.333 & 28.341 & 1 \\
    15    & 14    & 0.026 & 0.780 & 0.032 & 0.968 & 1.353 & 27.619 & 0.920 \\
    23    & 13    & 0.4   & 0.730 & 0.354 & 0.646 & 1.361 & 27.207 & 0.880 \\
    31    & 11    & 0.53  & 0.610 & 0.465 & 0.535 & 1.363 & 27.126 & 0.870 \\
    38    & 9     & 0.65  & 0.500 & 0.565 & 0.435 & 1.363 & 26.977 & 0.860 \\
    46    & 7     & 0.79  & 0.390 & 0.669 & 0.331 & 1.364 & 26.808 & 0.840 \\
    53    & 5     & 0.91  & 0.280 & 0.765 & 0.235 & 1.363 & 26.795 & 0.840 \\
    61    & 4     & 1.05  & 0.230 & 0.820 & 0.180 & 1.362 & 26.618 & 0.820 \\
    68    & 2     & 1.17  & 0.120 & 0.907 & 0.093 & 1.361 & 26.468 & 0.800 \\
    76    & 0     & 1.3   & 0     & 1     & 0     & 1.361 & 26.434 & 0.800 \\
    \end{tabular}
  \label{tbl:calCurve}
\end{table}

The calibration curves from both the refractive index observations as well as
the specific gravity ones are plotted in Figures @fig:calCurveRI and @fig:calCurveSG.
The data for both curves has been tabulated in Table \ref{tbl:calCurve}.

![Calibration Curve from Refractive Index Data](img/calCurveRI.png){#fig:calCurveRI}

![Calibration Curve from Specific Gravity Data](img/calCurveSG.png){#fig:calCurveSG}


\begin{table}[htbp]
  \centering
  \caption{Vapor Liquid Equilibrium Data}
    \begin{tabular}{ccccc}
    \textcolor[rgb]{ .122,  .286,  .49}{\textbf{xEtoh}} & \textcolor[rgb]{ .122,  .286,  .49}{\textbf{xw}} & \textcolor[rgb]{ .122,  .286,  .49}{\textbf{yEtoh}} & \textcolor[rgb]{ .122,  .286,  .49}{\textbf{yw}} & \textcolor[rgb]{ .122,  .286,  .49}{\textbf{T, oC}} \\
    \midrule
    0     & 1     & 0     & 1     & 100 \\
    0.019 & 0.981 & 0.17  & 0.83  & 95.5 \\
    0.0721 & 0.9279 & 0.3891 & 0.6109 & 89 \\
    0.099 & 0.9034 & 0.4375 & 0.5625 & 86.7 \\
    0.1238 & 0.8762 & 0.4704 & 0.5296 & 85.3 \\
    0.1661 & 0.8339 & 0.5089 & 0.4911 & 84.1 \\
    0.2337 & 0.7663 & 0.5445 & 0.4555 & 82.7 \\
    0.2608 & 0.7392 & 0.558 & 0.442 & 82.3 \\
    0.3273 & 0.6727 & 0.5826 & 0.4174 & 81.5 \\
    0.3965 & 0.6035 & 0.6122 & 0.3878 & 80.7 \\
    0.5198 & 0.4802 & 0.6599 & 0.3401 & 79.7 \\
    0.5732 & 0.4268 & 0.6841 & 0.3159 & 79.3 \\
    0.6763 & 0.3237 & 0.7385 & 0.2615 & 78.74 \\
    0.7472 & 0.2528 & 0.7815 & 0.2185 & 78.41 \\
    0.8943 & 0.1057 & 0.8943 & 0.1057 & 78.15 \\
    1     & 0     & 1     & 0     & 78.3 \\
    \end{tabular}
  \label{tab:vle}
\end{table}


## Calculations

Do crazy shit here

## Results and Discussion 

1. Ethanol and water form a minimum boiling azeotrope at a composition of $95.5
   \%$ by weight of ethanol @speight2005lange, @lide2003crc. Once this
   composition has been achieved, the liquid and vapour have the same
   composition, and no further separation is possible without using an
   entrainer. Absolute alcohol can be obtained using the process of heterogenous
   azeotropic distillation @seader2016separation. The addition of benzene to
   an ethanol-water mixture results in the formation of a minimum-boiling,
   heterogeneous ternary, azeotrope containing, by weight, $18.5 \%$ alcohol,
   $74.1 \%$ benzene, and $7.4 \%$ water, boiling at $64.85 ^\circ$C. Upon
   condensation, the ternary azeotrope separates into two liquid layers: a top
   layer containing $14.5 \%$ alcohol, $84.5 \%$ benzene, and $1 \%$ water, and
   a bottoms layer of $53 \%$ alcohol, $11 \%$ benzene, and $36 \%$ water, by
   weight. The benzene-rich layer is returned as reflux. The other layer is sent
   to a second distillation column for recovery and recycling of alcohol and
   benzene. Absolute alcohol, which has a boiling point above that of the
   ternary azeotrope, is removed at the bottom of the column.

## References
