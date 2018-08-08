# Continuous Distillation

## Objective

The objective is to study the process of continuous distillation in a sieve
plate column, for the separation of a water-ethanol mixture. The tray efficiency for the column, mass and energy balances, and heat loss should also be determined.

## Apparatus Required

*Equipment required:* Distillation column made of glass with perforated plates,
specific gravity bottle, specific gravity balance, Abbe refractometer, laboratory droppers, laboratory glassware.

The mixture to be separated is ethanol-water. The actual number of plates in the
distillation column is $12$. Metering pumps have been used for the feed and the
reflux.

## Theory

![Distillation Operation Using a Total Condenser and Partial Reboiler](img\distillation.PNG)

The general countercurrent-flow, multistage, binary-distillation operation
consists of a column containing the equivalent of N theoretical stages; a total
condenser in which the overhead vapor leaving the top stage is totally condensed
to give a liquid distillate product and liquid reflux that is returned to the
top stage; a partial reboiler in which liquid from the bottom stage is partially
vaporized to give a liquid bottoms product and vapor boil-up that is returned to
the bottom stage, and an intermediate feed stage @seader2016separation. By means
of multiple, countercurrent contacting stages arranged in a two-section cascade
with reflux and boil-up, it is possible to achieve a sharp separation between
the two components in the feed unless an azeotrope is formed, in which case one
of the two products will approach the azeotropic composition. For the
ethanol-water system, separation can only be achieved up to $95.5 \%$ ethanol.

### Assumptions

In order to plot the locus of all passing streams in the rectifying section as a
straight line of the form $y = mx + c$, the total molar flow rates $L$ and $V$
cannot vary from stage to stage. The following are the *McCabe-Thiele
assumptions*^[@seader2016separation,@gorak2014distillation].

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

$$ R = \frac{L}{D} $${#eq:}

### Rectifying Section

![Rectifying Section](img/1533580926428.png){#fig:rectSec}

A material balance for the light key over the envelope shown in figure
@fig:rectSec for the total condenser and stages $1$ to $n$ is as follows, where
$y$ and $x$ refer to vapor and liquid mole fractions, respectively, for the
light key:

$$ V_{n+l} y_{n+l} = L_n x_n + D x_D $${#eq:}

Solving for $y_{n+1}$, we get:

$$ y_{n+1} = \frac{L_n}{V_{n+1}} x_n + \frac{D}{V_{n+1}} x_D$${#eq:}

Where we note that:

- $L_0$ is the external reflux rate
- $D$ is the distillate rate
- $\frac{L_0}{D}$ is the reflux ratio, $R$

Additionally we know from the overall mass balance around the equipment envelope
that, 

$$V=L+D$${#eq:massVap}

From this, we may now note the relation between the operating line and the
reflux ratio, ie. @eq:opRe

$$\frac{L}{V}=\frac{L}{L+D}=\frac{L/D}{L/D+D/D}=\frac{R}{R+1}$${#eq:opRe}

Similarly,

$$\frac{D}{V}=\frac{D}{L+D}=\frac{1}{R+1}$${#eq:opRe1}

From equations @eq:massVap,@eq:opRe and @eq:opRe1 we now have the most used
form, that of @eq:opReFin

$$y=\left(\frac{R}{R+1}\right)x+\left(\frac{1}{R+1}\right)x_D$${#eq:opReFin}

### Stripping Section

![Stripping Section](img/strpSec.png){#fig:strp}

Analogous to the develop above, we shall step through the equations of note in
the stripping section, marked in @fig:strp. Vapor leaving the partial reboiler
is assumed to be in equi- librium with the liquid bottoms product, $B$, making
the partial reboiler an equilibrium stage. The vapor rate leaving it is the
boilup, $\bar{V}_{N+1}$, and its ratio to the bottoms product rate,
$V_B=\bar{V}_{N+1}/B$ is the *boilup ratio*. With the constant-molar overflow
assumption, V B is constant in the stripping section.

Since $\bar{L}=\bar{V}+B$, we have

$$\frac{\bar{L}}{\bar{V}}=\frac{\bar{V}+B}{\bar{V}}=\frac{V_B+1}{V_B}$${#eq:strp1}

$$\frac{B}{\bar{V}}=\frac{1}{V_B}$${#eq:strp2}

Similar to the section above we now have the final equation in @eq:strpFin.

$$y=\left(\frac{V_B+1}{V_B}\right)x-\left(\frac{1}{V_B}\right)x_B$${#eq:strpFin}

### Feed Conditions

The feed line equation is given by:

$$y = \frac{q}{q-1}x - \frac{z_F}{q-1}$${#eq:feedLine}

| **Feed condition**     | **f**       | **q**      | **q Calculation**                                                 |
| ---------------------- | ----------- | ---------- | ------------------------------------------------------------      |
| Subcooled liquid       | $f < 0$     | $q > 1$    | $q = [c_{P,L} (T_{bp} - T_F ) + \Delta H_{vap} ]/ \Delta H_{vap}$ |
| Liquid at bubble point | $0$         | $1$        | $q = \Delta H_{vap} / \Delta H_{vap} = 1$                         |
| Partially vaporized    | $0 < f < 1$ | $1< q < 0$ | $q = [(1 - f) \Delta H_{vap} ] / \Delta H_{vap}$                  |
| Vapor at dew point     | $1$         | $0$        | $q = 0$                                                           |
| Superheated vapor      | $f > 1$     | $q < 0$    | $q = - [c_{P,V} (T_F - T_{dp} )] / \Delta H_{vap}$                |

Table: Possible Feed Conditions and Corresponding $q$ Values^[@gorak2014distillation]. {#tbl:feedCond}

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

Using the McCabe Thiele method, the number of stages were plotted in @fig:totalReflux and @fig:partialReflux.

![Total Reflux](img\totalReflux.png){#fig:totalReflux}

![Partial Reflux](img\partialReflux.png){#fig:partialReflux}

## Calculations

#### Specific Gravity Calculations

Weight of the empty bottle $=18.911g$

The weight of $10g$ liquid in the bottle is the sum of the weight of the liquid and the weight of the empty bottle. To get the weight of only the liquid, the weight of the empty bottle must be subtracted from the reading obtained from the specific gravity balance. 

Weight of liquid water $=28.341-18.911=9.43g$

Specific gravity of the liquid $=\frac{9.43}{10}=0.943g/mL$ 

### Calibration Curve 

From the calibration curves Figures @fig:calCurveRI and @fig:calCurveSG, relations for the mole fractions of ethanol can be determined:

$$x_{Eth} = \frac{(RI-1.3428)}{0.04168}$${#eq:cal1}

$$x_{Eth} = \frac{(SG-0.94122)}{0.14565}$${#eq:calSG}

@eq:cal1 is used for lower mole fractions of ethanol, while @eq:calSG is used for higher mole fractions.

### Feed Line Equation

Refractive Index of the feed mixture $= 1.357 = 0.36$ mole fraction

The bubble point of feed mixture must be determined. The temperature of the feed is room temperature; i.e. $30 ^\circ C$.

The Antoine equations for ethanol ^[@ambrose1975vapour] and water ^[@liu1970vapor] are :

$$log_{10}(P^*) = 4.92531-\frac{1432.526}{(T-61.819)}$${#eq:antEth}

$$log_{10}(P^*) = 3.55959 - \frac{643.748}{(T-198.043)}$${#eq:antWater}

where, 

* $P$ is the vapour pressure in bar
* $T$ is the temperature in Kelvin

Rault's law is given by:

$$P = P_A^*x_A + P_B^*x_B$${#eq:rault}

Using @eq:antEth , @eq:antWater, @eq:rault we obtain, at atmospheric pressure:

$$760 = x_{Eth} [10^{4.92531-1432.526/(T-61.819)}] + (1-x_{Eth}) [10^{3.55959-643.748/(T-198.043)}]$${#eq:calc1}

Using @eq:calc1, we calculate the bubble point of the feed to be $363.2 K = 90.2 ^\circ C$.

Specific heat capacity of the mixture is given by: 

$$c_{p,mix} = x_{Eth} c_{p,Eth} + (1-x_{Eth}) c_{p,wat}$${#eq:calc2}

$\Delta H_{vap}$ of the mixture is given by:

$$\Delta H_{vap,mix} = x_{Eth} \Delta H_{vap,Eth} + (1-x_{Eth}) \Delta H_{vap,wat}$${#eq:calc3}

Using the equations from Table @tbl:feedCond, we calculate:

$$q = 1.133$${#eq:subcool}

From @#eq:subcool and Table @tbl:feedCond, it can be concluded that the feed is *subcooled*.

Using @eq:feedLine, the equation for the feed line can be obtained from the calculated value of $q$:

$$y = 8.52x -2.707$${#eq:calc4}

### Total Reflux Condition

Specific gravity of distillate $=0.82$

Refractive index of bottoms $=1.344$

$x_{Eth}$ for distillate $=0.823$

$x_{Eth}$ for the bottoms $=0.028$

#### Rectifying Line

For the total reflux condition, $R \rightarrow \infty$, and thus, on substituting into @eq:opReFin, we obtain:

$$y_{n+1} = x_n$${#eq:calcrc1}

#### Stripping Line

$$V=L+D$${#eq:calbasic}

where:

* $V$ and $L$ are the constant molar overflows
* $D$ is molar flow rate of the distillate

Since $D=0$, $V=L$.

$$y_{m+1} = x_m$${#eq:calcst1}

#### Tray Efficiency

Number of trays from the plot $= 9$

Actual number of trays $=12$

The tray efficiency is calculated as:

$$Efficiency = \frac{9}{12} \times 100 = 66.67\%$$

### Partial Reflux Condition

Specific gravity of distillate $=0.82$

Refractive index of bottoms $=1.343$

$x_{Eth}$ for distillate $=0.823$

$x_{Eth}$ for the bottoms $=0.02$

Reflux ratio $R=2.96$

#### Material Balance

##### Overall Material Balance

$$F=D+B$${#eq:bal}

From the observation table, $F=8.57mL/min$, $B=6mL/min$, $D=2.47mL/min$

The total feed supplied is the sum of the primary feed and the secondary feed.

Secondary feed $=500-330=170mL$

Primary feed $=1500mL$

Total feed $=1500+170=1670mL$

Distillate volume $=160mL$

Total volume of bottoms collected $=621mL$

According to the ideal material balance equation in @eq:bal, the L.H.S and R.H.S. are calculated as:

$$L.H.S.=F=1670mL$${#eq:stuff1}

$$R.H.S.=B+D=160+621=781mL$${#eq:stuff1}

Density of ethanol $=0.789g/mol$

Density of water $=1.0g/mol$

Density of the feed, with $z_F$ of $0.36 = z_F\rho_{Eth}+(1-z_F)\rho_{wat}=0.924g/mol$

Density of distillate $=x_D\rho_{Eth}+(1-z_F)\rho_{wat}=0.826g/mol$

Density of the bottom $=x_w\rho_{Eth}+(1-z_F)\rho_{wat}=0.996g/mol$

Molecular weight of the feed $=0.36\times46+(1-0.36)\times18=28.08g/mol$

Molecular weight of the distillate $=0.823\times46+(1-0.823)\times18=41.04g/mol$

Molecular weight of the bottom $=0.02\times46+(1-0.02)\times18=18.56g/mol$

Moles in the feed $=53.97mol$

Moles in the distillate $=3.22mol$

Moles in the bottom $=33.32mol$

##### Component Material Balance

The component material balance is given by:

$$Fz_F=Dx_D+Bx_w$${#eq:compMat}

On solving @eq:compMat, we get:

$$L.H.S.=53.97\times0.36=19.43mol$${#eq:compMat1}

$$R.H.S.=3.22\times0.823+33.32\times0.02=3.31mol$${#eq:compMat2}

#### Energy Balance

Heat capacity of water $=75.6J/molK$

Heat capacity of the ethanol $=111.46J/molK$

Heat capacity of the distillate $=x_Dc_{p,Eth}+(1-x_D)c_{p,wat}=105.11J/molK$

Heat capacity of the feed $=z_Fc_{p,Eth}+(1-z_F)c_{p,wat}=88.51J/molK$

Heat capacity of the bottom $=x_wc_{p,Eth}+(1-x_w)c_{p,wat}=76.31J/molK$

##### Energy Input

Energy given to the reboiler $=590.9-590.1=0.8kWh=0.8\times3600kJ=2889kJ$

##### Energy Output

The feed is at room temperature; i.e. at $30^\circ C$.

Temperature of the distillate $=74 ^\circ C$

Average temperature of the bottom $=0.5 \times (98+114)=106 ^\circ C$

Energy of the distillate $=mc_p \Delta T=14.89kJ$

Energy of the bottom $=mc_p \Delta T=33.32 \times 76.31 \times (106-30)=193.24kJ$

Energy lost in the condenser $= \rho V_{flow}c_p \Delta T \times time = 2196.6kJ$

##### Total Heat Lost

Total heat loss $=2889-(14.89+193.24+2196.6)=484.3kJ$

#### Rectifying Line

Using @eq:opReFin, the rectifying line obtained is:

$$y_{n+1}=0.747x_n+0.25$${#eq:partial1}

#### Stripping Line

From @eq:calbasic, @eq:strpFin, we obtain:

$$y_{m+1}=\frac{L}{(L+D)}x_m-\frac{B}{(L+D)}$${#eq:partial2}

On solving @eq:partial2, the stripping line can be obtained:

$$y_{m+1}=0.748x_m-0.613$${#eq:partial3}

#### Tray Efficiency

Number of trays from the plot $= 11$

Actual number of trays $=12$

The tray efficiency is calculated as:

$$Efficiency = \frac{11}{12} \times 100 = 91.67\%$$

## Results and Discussion 

1. The overall material balance indicated a loss in mass. This can be explained by a mass accumulation inside the column, which may be a result of non-ideal tray hold-up, which does not remain constant throughout the operation.
2. When the column reflux ratio was changed from total reflux to partial reflux, a rise in the reboiler temperature, from an average of $91 ^\circ C$ to $106 ^\circ C$.
3. A higher number of trays was required for the partial reflux case, consistent with the decline of driving force for the separation.
4. The heat loss during the separation was about $16.7\%$. This may be attributed to insufficient insulation.
5. Ethanol and water form a minimum boiling azeotrope at a composition of $95.5\%$ by weight of ethanol ^[@speight2005lange], [@lide2003crc]. Once this composition has been achieved, the liquid and vapour have the same composition, and no further separation is possible without using an entrainer. Absolute alcohol can be obtained using the process of heterogenous azeotropic distillation @seader2016separation. The addition of benzene to an ethanol-water mixture results in the formation of a minimum-boiling, heterogeneous ternary, azeotrope containing, by weight, $18.5 \%$ alcohol, $74.1 \%$ benzene, and $7.4 \%$ water, boiling at $64.85 ^\circ$C. Upon condensation, the ternary azeotrope separates into two liquid layers: a top layer containing $14.5 \%$ alcohol, $84.5 \%$ benzene, and $1 \%$ water, and a bottoms layer of $53 \%$ alcohol, $11 \%$ benzene, and $36 \%$ water, by weight. The benzene-rich layer is returned as reflux. The other layer is sent to a second distillation column for recovery and recycling of alcohol and benzene. Absolute alcohol, which has a boiling point above that of the ternary azeotrope, is removed at the bottom of the column.

## Conclusions

1. The value of $q$ obtained for the feed is $1.133$, which indicates that the feed is in the subcooled condition. This is in accordance with the feed actually used in the experiment, which was a liquid at room temperature. 
2. In the case of partial reflux, the tray efficiency is $91.67\%$, which is higher than the tray efficiency $66.67\%$ for the total reflux condition. This may be attributed to the ease of separation for the two cases. 

## References
