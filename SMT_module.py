from Question_class import Question
def chemistry_year_1978():
    question_prompt=["""1.Which of the following statements is  correct?
    A. The average kinetic energy of gas is directly  proportional to it's temperature..
    B. At constant temperature the volume of a gas increases as pressure increases 
    C.The pressure of a gas is inversely proportional tto it's volume 
    D. The temperature of a gas is directly proportional to it's volume 
    E. The collisions of molecules with each other are elastic .
    ""","""2.The molarity of 2% by weight of aqueous solution of H₂SO₄ (molecular weight=98) is
    A. 4.55
    B. 3.55
    C. 2.55
    D. 1.55
    E. 0.55
    ""","""3.Zinc oxide is a..
    A. basic oxide 
    B. acidic oxide
    C. amphoteric oxide 
    D. neutral oxide
    E. reactive oxide
    ""","""4.When sodium chloride and metallic sodium are each dissolved in water
    A. both processes are exothermic 
    B. both processes endothermic
    C. the dissolution of metallic sodium is endothermic
    D. the dissolution of metallic sodium is exothermic 
    E. the dissolution of sodium chloride is explosive
    ""","""5. The periodic classification of the elements is an arrangement of the elements in order of their 
    A. atomic weights
    B. isotopic weights
    C. molecular weights 
    D. atomic numbers
    E. atomic masses 
    ""","""6. The reaction between sodium hydroxide and sulphuric acid solutions, what volume of 0.5 molar
     sodium hydroxide would exactly neutralise 10cm3 of 1.25 molar sulphuric acid?
     A. 5cm3
     B. 10cm3
     C. 20cm3
     D, 25cm3
     E. 50cm3
     ""","""7.A small quantity of solid ammonium chloride(NH4Cl) was heated gently in a test tube,
     the solid gradually disappared to produce a mixture of gases. Later a white cloudy deposit was was observed 
     on the cooler part of the test tube. The ammonium chloride is  said to have undergone
     a. distillation
     b. sublimation 
     c. precipitation
     d. evaporation
     e. decomposition
     ""","""8. Elements P,Q,R,S have 6, 11, 15 and 17 electrons respectively, therefore, 
     a. P will form an electrovalent bond with R
     b. Q will form a covalent bond with S
     c. R will form an electrovalent bond with S
     d. Q will form an electrrovalent bbond with S
     e, Q will form a covalent bond with R
     ""","""9. An element X forms the following compounds with chlorine; XCl4, XCl3, XCl2.
     This illustrates the
     a. law of multiple proportions
     b. law of chemical proportions 
     c. law of simple proportions 
     d. law of conservation of mass
     ""","""10. The oxidation state of chlorine in potassium chlorate is:
     a. +1
     b. +2
     c. +3
     d. +5
     e. +7
     ""","""11. When air, which contains the gases: oxygen, nitrogen, carbondioxide water vapour and the rare gases,
     is passed through alkaline pyrogallol and then over quickilime, the only gases left are:
     a. nitrogen and carbodioxide 
     b. the rare gases 
     c. nitrogen and oxygen
     d. nitrogen and the rare gases
     e. nitrogen, carbondioxide  and the rare gases
     ""","""12. When heat is absorbed during a chemical reaction the reaction is said to be..
     a. thermodynamic
     b. exothermic 
     c. isothermal
     d. endothermic
     e. thermostatic
     ""","""13. When large hydrocarbon molecules are heated at high temperature in the presence of a catalyst to
     give smaller molecules, the process is known as 
     a. disintegration
     b. polymerization
     c. cracking
     d. degradation
     e. distillation
     ""","""14. The pH of four solutions W, X, Y, Z are 4,6,8,10 respectively, therefore..
     a. None of these solutions is acidic 
     b. The pH of Y is more acidic by addition of distilled water
     c. Z is the most acidic solution
     d. W is the most acidic solution 
     e. X is neutral
     ""","""15. When each of the nitrates of potassium, magnesium and iron are heated 
     a. all nitrates decompose to their oxide
     b. the nitrate of magnesium gives the nitrite and oxygen
     c. the nitrate of magnesium and iron give the oxides
     d. the nitrate of iron gives the nitrite and oxygen
     e. the nitrate of magnesium is not decomposed
     ""","""16. Which of the following metals cannot replace hydrogen from water or steam
     a. sodium 
     b. magnesium
     c. iron
     d. calcium
     e. copper
     ""","""17.  A sample of hard water contains some calcium sulphate and calcium hydrogen carbonate. The total
     hardness may therefore be removed by
     a. boiling of water 
     b. adding of excess calcium hydroxide
     c.  adding a calculated amount of calcium hydroxide
     d. adding sodium carbonate
     e. adding magnesium hydroxide
     ""","""18. During electrolysis of copper II sulphate between platinum electrodes, if litmus solution
     is added to the anode compartment 
     a. The litmus turns blue  but no gas is evolved
      b. The litmus turns blue and oxygen is evolved 
      c. The litmus turns blue and hydrogen is evolved 
      d. The litmus turns red and oxygen is evolved 
      e.. The litmus red and then becomes colourless
      ""","""19. The reaction between an organic acid and an alcohol in the the presence of an acid
      catalyst is known as:
      a. saponification
      b. dehydration
      c. esterification 
      d. hydrolysis
      e. hydration
      ""","""20. The IUPAC names for compounds CH3COOH and CH2 are respectively:
      a. acetic acid and ethane
      b. ethanoic acid and ethene 
      c. methanoic acid and ethylene
       d. ethanol and ethene 
       e. acetic acid and ethylene 
       ""","""21. If 30cm3 of oxygen diffuses through a porous pot in 7 seconds, how long will it take 60cm3 of
       chlorine to diffuse through the same pot, if the vapour densities of oxygen and chlorine are 16 and 36 respectively
       a. 9.3 seconds
       b. 14 seconds
       c. 21 seconds
       d. 28 seconds 
       e. 30.3 seconds
       ""","""22. Brass and bronze are both metallic alloys. Which of the following constituents is common to both alloys
       a. Tin
       b. Zinc
       c. Copper
       d. Lead
       e. Aluminium
       ""","""23. Which of the following gases may not be dried with concentrated sulphuric acid?
       a. HCl
       b. N2
       c. Cl2
       d. SO2
       e. NH3
       ""","""24. Which of the following reactions does not take place in smelting of iron in a blast furnace
       a. CaCO3(s) → CaO(s) + CO2(g)
       b. C(s) + O2(g) → CO2(g)
       c. 3Fe + 2O2(g) → FeO4(s)
       d. SiO2(g) + CaO(s) → CaCO3(s)
       e. CO2(g) + C(s) → 2CO(g)
       ""","""25. Which of the following is not a member of the homologous series of the paraffins(alkanes)
       a. C3H8
       b. C5H12
       c.  C7H16
       d. C15H32
       E. C24H48
       ""","""26. When ammonia and hydrogen ion bond together to form ammonium ion,
       the bond formed is called 
       a. ionic bond
       b. electrovalent bond
       c. covalent bond
       d. co-ordinate bond
       e. hydrogen bond 
       ""","""27. An example of an alcohol is
       a. CCl4
       b. CH3COOH
       c. CHCl3
       d. C2H6
       e. CH3OH
       ""","""28. The nucleus of an atom contains
       a. protons only
       b. neutrons only
       c. protons and electrons
       d. neutrons and electrons
       e. protons and neutrons
       ""","""29. Hypochlorous acid is used as bleach because 
       a. it is a strong acid
       b. it yields chlorine readily in pure water
       c. it is an oxidizing agent
       d. it is a weak acid 
       e. it is an reducing agent
       ""","""30. The normal boiling point of a liquid is defined as
       a. the temperature at which its vapour pressure equal the atmospheric pressure
       b. The temperature at which bubbles begin to form
       c. the temperature at which the vapour pressure equals 1 temperature
       d. the temperature at which the rate of condensation of vapour equals the rate of vaporization of the liquid
       e. the temperature at which the space above the liquid is saturated 
       ""","""31. Which of the following compounds will form a solution if exposed to air
       a. Na2CO3.10H2O
       b. NaNO3
       c. CuSO4
       d. Cacl2
       e. NaSO4.10H2O
       ""","""32. The most common type of chemical reaction which alkanes undergo is 
       a. substitution 
       b. addition
       c. condensation
       d. polymerization
       e. double decomposition
       ""","""33. Consider the following exothermic reaction 2SO2(g) + O2(g) ⇌ 2SO3(g). If the temperature
       of the reaction is reduced from 800oC to 500oC, and no other change takes place, then 
       a. the reaction rate increases 
       b. concentration of SO3 decreases 
       c. concentration of SO3 increases
       d. SO2 gas becomes unreactive
       e. O2 gas become unreactive
       ""","""34. If excess zinc is added to a blush green solution of copper(II) sulphate, and the excess zinc filtered 
       off after completion of reaction, a colourless solution is obtained because
       a. both zinc and copper are metals
       b. the sulphate radical and the zinc ion are divalent
       c. zinc is more electropositive than copper 
       d. both zinc and copper form depositive ions in solution 
       e. zinc is a reducing agent
       ""","""35. Three solutions contain carbonate, sulphate, an sulphide ions respectively. One test
       that will identify just ONE of them completely is by addition to each of them of
       a. barium chloride solution
       b. dilute hydrochloric acid
       c. lead nitrate solution
       d. calcium chloride solution
       e. sodium hydroxide solution
       ""","""36. Two gas cylinders contain ethylene (ethene) and acetylene respectively. One test which can be use to distinguish between them is by
       a. passing each gas through bromine water
       b. passing each gas through dilute potassium
       c. passing each gas through silver nitrate solution
       d. passing each gas through ammonical paper (I) chloride solution
       e. treating each gas catalytically with excess hydrogen gas
       ""","""37. Consider the following equation H2O + (2Fe2+) + Cl2 ⇌ 2Fe3+ + 2Cl- + H2O. 
       The only ion which behaves as an oxidizing agent is 
       a. Fe2+
       b. Cl2
       c. Fe3+
       d. Cl-
       e. H2O
       ""","""38. If hydrogen sulphide gas is passed into a solution of pure iron chloride
       a yellow deposit appears. If the deposit is filtered, a pale green solution is left behind
       The pale green solution is
        a. a dilute sulphuric acid
        b. dilute hydrochloric acid
        c. unreacted hydrogen sulphide in water
        d. iron (III) chloride
        e.  iron (II) chloride
        ""","""39. Which one of the following changes is physical?
        a. Adding iron filling to aerated water
        b. Adding sodium metal to water
        c. Cooling a solution of iron (II) sulphate to obtain the hydrated salt
        d. Cooling water to obtain ice
        e. Burning the domestic gases (Utilgas) for cooking
        ""","""40. By means of filtration, one component can be obtained pure from an aqueous mixture of sodium chloride and
        a. potassium nitrate
        b. sand
        c. lead nitrate
        d. sugar(glucose)
        e. starch
        ""","""41. Five atoms T,W,X,Y,Z, consists of the following particles
                      T    W    X    Y    Z   
        Proton   13   16   17   19   20
        Electron 13  16   17   19   20
        Neutron 14  16   35   20   20
        
        Which of the following can be described by the
        followin properties: Relative atomic mass is greater than 40,
        it has odd atomic number and forms a unipositive ion in solution
        a. T
        b. W
        c. X
        d. Y
        e. Z
        ""","""42. A solid X when heated gives off a brown gas. If X is soluble in excess sodium hydroxide
        solution but insoluble in excess ammonium hydroxide solution then X is
        a. a basic lead carbonate
        b. lead (II) nitrate
        c. sodium carbonate
        d. zinc nitrate
        e. sodium nitrate
        ""","""45. In titration involving sodium hydroxide solution and dilute hydrochloric acid
        where would you place the base?
        a. beaker
        b. Conical flask
        c. Burette
        d. Standard flask 
        e. measuring cylinder
        ""","""46. A gas jar was inverted over burning yellow phosphorus floating over water in a beaker
        After burning, the water level was found to rise in the gas jar. The water level rises because
        a. pressure inside the gas jar is greater than the pressure outside it
        b. the air in the gas jar had been used by burning
        c. oxygen in the gas jar had been used up by burning
        d. nitrogen in the gas jar had been used up by burning
        e. the temperature in the jar had risen considerably
        ""","""47. You are provided with five gas jars containing SO2, CO2, H2, CO and NO respectively. Select a test
        from a to e which will identify any one of the gases completely
        a. pass each gas into lime water
        b. pass each gas into water and test with ltmus paper
        c. pass each gas into concentrated sulphuric acid 
        d. expose each gas to atmospheric air
        e. expose each gas to fumes of hydrogen chloride
        ""","""48. Which of the following substances would you see as an indicator in the titration of sodium carbonate 
        solution against hydrochloric acid (complete neutralization) ?
        a. litmus paper
        b. phenolphthalein
        c. methyl orange
        d. Universal indicator
        e. None of these
        ""","""49. Five elements R,T,W,X and Y form the following compounds: a basic hydride R.H,
        an acidic hydride YH, amphoteric oxide W2O3, XO2. Which of the elements is an alkali?
        a. R
        b. T
        c. W
        d. X
        e. Y
        ""","""50.The size (diameters) of five atoms are in the order: R<T<W<X<Y, Y being the largest.
        If each atom has an electron situated in its circumference, and neglecting other factors, which of the atoms will
        lose its electron most reluctantly
        a. R
        b. T
        c. W
        d. X
        e. Y"""]
    question=[Question(question_prompt[0],"A"),
              Question(question_prompt[1],("A"or"b" or "c" or "d" or "e")),
              Question(question_prompt[2],"C"),
              Question(question_prompt[3],"D"),
              Question(question_prompt[4],'D'),
              Question(question_prompt[5],"E"),
              Question(question_prompt[6],"B"),
              Question(question_prompt[7],"D"),
              Question(question_prompt[8],"A"),
              Question(question_prompt[9],"D"),
              Question(question_prompt[10],"D"),
              Question(question_prompt[11],"D"),
              Question(question_prompt[12],"C"),
              Question(question_prompt[13],"D"),
              Question(question_prompt[14],"C"),
              Question(question_prompt[15],"E"),
              Question(question_prompt[16],"D"),
              Question(question_prompt[17],"D"),
              Question(question_prompt[18],"C"),
              Question(question_prompt[19],"B"),
              Question(question_prompt[20],"C"),
              Question(question_prompt[21],"C"),
              Question(question_prompt[22],"E"),
              Question(question_prompt[23],"C"),
              Question(question_prompt[24],"E"),
              Question(question_prompt[25],"D"),
              Question(question_prompt[26],"E"),
              Question(question_prompt[27],"E"),
              Question(question_prompt[28], "C"),
              Question(question_prompt[29],"A"),
              Question(question_prompt[30],"D"),
              Question(question_prompt[31],"A"),
              Question(question_prompt[32],"C"),
              Question(question_prompt[33],"C"),
              Question(question_prompt[34],"C"),
              Question(question_prompt[35],"D"),
              Question(question_prompt[36],"B"),
              Question(question_prompt[37],"E"),
              Question(question_prompt[38],"D"),
              Question(question_prompt[39],"B"),
              Question(question_prompt[40],"D"),
              Question(question_prompt[41],"B"),
              Question(question_prompt[42],"B"),
              Question(question_prompt[43],"C"),
              Question(question_prompt[44],"A"),
              Question(question_prompt[45],"C"),
              Question(question_prompt[46],"A"),
              Question(question_prompt[47],"A")]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            if answer.upper() == question.answer:
                print("Corrrect.Yeah! you got it that's the spirit. Keep it up\n\n")
                score += 2
            else:
                print("Wrong, the answer is", question.answer, "Awwn! maybe you will have luck in the next one\n\n")
        percent = str(((score) / (len(questions * 2)) * 100)//1) + "%"
        print("You got " + percent + " correct")

    run_test(question)



def chemistry_year_1979():
    question_prompt2=["""1. An organic compound X has the following properties: 1. It is not miscible with water 
    2. it has boiling point of 77⁰C 3. It has a sweet odour 4. It is insoluble in sodium hydrogen carbonate solution 
    5. It does not decolourize bromine water. X is therefore
    a. Methane
    b. Ethanoic acid
    c. Ethene
    d. Ethyl ethanoate 
    e. carbon tetrachloride
    ""","""2. Which are the correct IUPAC names for H-CO₂CH₃ and CH≡CH
    a. Methyl methanoate and ethene
    b. Methanoic acid and ethyne
    c. Ethyl methanoate and ethyne
    d. Methyl methanoate and ethyne
    e. Ethanoic acid and ethene
    ""","""3. Which of the following substances are all made by the process of polymerization?
    a. Nylon and soap.
    b. Ethnaoic acid, margarine and ethanol 
    c. Nylon and artificial rubber 
    d.Soap and butane 
    e. Margarine and nylon
    ""","""4.The reaction of zinc with copper (ll) ions in aqueous solution can be represented as follows: Cu2+(aq) +Zn(s)-> Cu(s) + Zn2+. 
    Which of the following is the most complete description of this reaction?
    a. Copper (ll) ions are being reduced.
    b. Zinc is being oxidized.
    c. Copper (ll) and zinc are being reduced 
    d. Copper (ll) ions and zinc are being oxidized
    e. Copper (ll) ions are being reduced and zinc oxidized
    ""","""5. The oxidation state of manganese in potassium permanagate is 
    a. +7
    b. +5
    c.+3
    d. +2
    e. +1
    ""","""6. When carbondioxide is bubbled into lime water a white prepicipate is formed.
    If the passage of the gas is continued the precipate disappears.The reason for this is
    a. Calcium carbonate is formed which on reaction dissolves
    b. Calcium hydrogen carbonate is precipitated and then dissolves
    c. Calcium carbonate is formed which on reaction with further carbon dioxide forms soluble calcium hydrogen carbonate 
    d. Concentration of the solution has occurred with the deposition of calcium hydroxide
    e. The solution has become saturated and solid carbon dioxide has been deposited.
     ""","""7. The following reactions are stages in important industrial processes: l. N2(g) + 3H2(g) ⇌ 2NH3(g) ΔH is negative
     II. 2SO2(g) + O2(g) ⇌ 2SO3(g) ΔH is negative
     III. N2(g) + O2(g) ⇌2NO(g) ΔΗ is positive.
     Which of the above forward reactions is favored by (I) a decrease in the concentration of the pressure and
     (II) an increase in temperature
     a. I
     b. II
     c. III
     d. I and II
     e. I and III
     """ ,"""8. The IUPAC name for                           
                                                                   CH
                                                                     |
                                                        CH₃— C —CH = CH₂
                                                                     |
                                                                    H
    is 
    a. 2-methylbut-3-ene
    b. 2-methylbut-4-ene
    c. 3-methylbut-2-ene
    d. 3-methylbut-1-ene
    e. 3-methylpent-1-ene
    ""","""9. Methanoic acid mixes with water in all proportions and has about the same boiling 
    point as water. Which of the following methods would you adopt to obtain pure water from a mixture
    of sand, water and methanoic acid?
    a. fractional distillation
    b. filtration followed by distillation
    c. Neutralisation with sodium hydroxide followed by distillation
    d. Neutralisation with sodium hydroxide followed by filtration
    e. Esterification with ethanol followed by distillation
    ""","""10. Which of the following statements applies during
    the electrolysis of sodium hydroxide solution using platinum electrodes
    a. Na+ ion are discharged at the cathode 
    b. Hydrogen ions are discharged at the anode
    c. The concentration of sodium hydroxide decreases at both electrode compartments
    d. The concentration of sodium hydroxide increases at the cathode only
    e. The concentration of sodium hydroxide increases at the anode only
    ""","""11. Which of the following statements is true? When the potassium atom forms its ion 
    a. it gains one electron and becomes neutral
    b. its atomic number decreases 
    c. it achieves electronic configuration of argon
    d. it loses one proton 
    e. it loses one neutron
    """,""" 12. Which of the following contains two amphoteric oxides?
    a. Sodium oxide, Zinc oxide, Magnesium oxide
    b.Aluminium oxide, Calcium oxide, Zinc oxide
    c. Potassium oxide, Lithium oxide, Carbondioxide
    d. Silver oxide, Lead oxide, Sodium oxide
    e. Sulphur dioxide, Aluminium oxide, Carbon monoxide
    ""","""13. Helium atoms are chemically unreactive because 
    a. there are no electrons around the nucleus
    b. the number of protons equals the number of electrons
    c. there are equal number of protons and neutrons in the nucleus
    d. The outer electron shells are completely filled
    e. The atoms contain only protons 
    ""","""14. 50cm³ of hydrogen are sparked with 20cm³ of oxygen at 100⁰C and one atmosphere.
    The total volume of the residual gases in 
    a. 50cm³
    b.10cm³
    c. 40cm³
    d. 30cm³
    e. 70cm³
    ""","""15. How many grams of HBr would exactly be required to react with two grams of propyne?(C=12, H=1, Br=80)
    a. 4.1g
    b. 6.1g
    c. 8.1g
    d.10.1g
    e.16.2g
    ""","""16. When ammonium, potassium and calcium carbonates are each seperately heated 
    a. none of them will decompose
    b. each of them will decompose to give carbondioxide and the respective oxide
    c. ammonium carbonate and potassium carbonate will not decompose
    d. only ammonium carbonate and calcium carbonate will decompose to carbondioxide and the respective oxide   
    e. ammonium carbonate will decompose to give carbondioxide, water and ammonia
    ""","""18. If chlorine gas is bubbled into water and then this yellowish-green solution is exposed
    to bright sunlight for a while 
    a. the solution wil give out chlorine gas and hydrogen chloride gas
    b. the solution will produce 
    c. The solution will give out oxygen thereby producing hypochlorous acid 
    d. The solution will give out oxygen gas leaving behind aqueous hydrochloric acid 
    e. The solution is  decomposed,giving out oxygen, hydrogen and chlorine 
    ""","""19. 12g of solid potassium chlorate (KClO₃) were added to 40g of water
     and heated to dissolve all the solid. As the solution cools, crystals of potassium chlorate started
     at 66⁰C. The solubility of potassium chlorate at 66⁰C is therefore 
    a. 66
    b. 33
    c. 10
    d. 20
    e. 30
    ""","""20. In the electrolysis of the dilute sulphuric acid using platinum electrodes, the products obtained at the anode and cathode are:
                      Anode                     Cathode
     a.              Sulphur                   Hydrogen   
     b.            Hydrogen                  Oxygen
     c.             Oxygen                   Hydrogen
     d.           Hydrogen                Sulphate ions
     e.            Sulphur                     Oxygen
     ""","""21. The empirical formula of an oxide of nitrogen containing 30.4 per cent of nitrogen is
     a. N₂O₂
     b. NO
     c. NO₂
     d. N₂O
     e. N₂O₃ (N=14.0, O=16.0
     ""","""22. When a piece of charcoal enclosed in a cylinder containing air is ignited 
     a. the total volume of air is increased 
     b. the relative amount of oxygen present is increased
     c. the relative amount of nitrogen present is decreased 
     d. the relative amount of carbondioxide present is increased
     e. the ratio of oxygen to nitrogen in the system is increased
     ""","""23. Indicate which of the following statements is not true as we move left to
     right on the periodic table
     a. atomic number of elements increase
     b. atomic mass of elements increase
     c. electropositive character of elements increase
     d. electronegative character of elements increase
     e. number of electrons in the outermost orbits of the elements increases
     ""","""24. 0.1 Faraday of electricity was passed through a solution of copper (II) sulphate. The maximum weight of
     copper deposited on the cathode would be
     a. 64.0g
     b. 32.0g
     c. 16.0g
     d. 6.4g
     e. 3.2g (Cu = 64
     ""","""25. Which one of these compounds will not give an oxygen gas on heating
     a. Manganese dioxide
     b. Hydrogen peroxide
     c. Zinc nitrate
     d. Sodium nitrate
     e. Ammonium nitrate
     ""","""26. In the extraction of aluminium from purified bauxite by electrolysis, cryolite is used because
     a. Manganese dioxide
     b. Hydrogen peroxide
     c. Zinc nitrate
     d. Sodium nitrate 
     e. Ammonium nitrate
     ""","""27. In the redox reaction 2Fe² + Cl₂⇌2Fe³ + 2Cl- 
     a. Cl₂ is reduced because it has lost electrons
     b. Cl₂ is reduced because its oxidation number has decreased
     c. Cl₂ is reduced because its molecule is changed to two ions 
     d. Fe² is reduced because it has lost electrons
     e.Fe² is reduced because it has gained electrons
     ""","""28. An anhydride is 
     a. a compound which has no water of crystallization 
     b. an oxide whose solution in water has a pH greater than 7
     c. an oxide whose solution in water has a pH less than 7
     d. an oxide that has hydrogen atoms
     e. an amphoteric  oxide
     ""","""29. In which of the following reactions is sulphur dioxide acting as an oxidizing agent?
      a. SO₂ + 2HNO₃ → H₂SO₄ + NO₂ +Heat
      b. 2SO₂ + 2H₂O + O₂ → 2H₂SO₄
      c. SO₂ + 2H₂O + Cl₂ → H₂SO₄ + 2HCl
      d. SO₂ + 2H₂S → 3S + 2H₂O
      e. SO₂ + H₂O → H₂SO₃
      ""","""30. Calcium hydroxide and ammonium chloride when heated together will give an
      important product. This compound may be obtained dry by
      a. dissolving it in water, recrystallizing it and then drying in the oven
      b. passing it through a concentrated aqueous solution of sodium hydroxide
      c. passing it through concentrated sulphuric acid
      d. passing it through calcium oxide
      e. passing it through anhydrous calcium chloride
      ""","""31. Starch can be converted to ethyl alcohol by
      a. distillation
      b. fermentation
      c. isomerization
      d. cracking
      e. cooking
      ""","""32. The reaction between hydrogen and iodine may be represented by the equation
      H₂(g) + I₂(g) → 2HI(g), and is exothermic. Therefore 
      a. an increase in temperature favours the forward reaction 
      b. an increase in pressure favours the backward reaction
      c. both pressure and temperature must be increased to favour the forward reaction
      d. a decrease in temperature will favour the forward reaction
      e. a decrease in pressure and an increase in temperature and will favour the forward reaction
      ""","""33. weighed salts Y and Z  were left exposed in the laboratory overnight. In the morning,
      Y had gained weight, and Z had become liquid. What conclusion could be drawn about the nature of the 
      two salts 
      a. Z is efflorescent
      b. Y and Z are efflorescent 
      c. Y and Z are deliquent 
      d. Y and Z hygroscopic 
      e. Y is deliquescent 
      ""","""34. In the manufacture of iron in the blast furnace, iron (III) oxide is mixed with coke and
      limestone,and different reactions occur in the process. Which of the following statements is true
      with respect to these reactions 
      a. The coke is a powerful reducing agent and easily converts the iron oxide to iron
      b. The calcium carbonate reacts with SiO an earthly impurity in the ore to form calcium silicate
      c. The coke will reacts with the iron produced to form steel 
      d. All the carbondioxide required in the process comes from the decomposition of the calcium carbonate
      e. The calcium carbonate decomposes to give calcium oxide which then forms calcium silicate with the earthly impurities
      ""","""35. Which of the following statements is true 
      a. An increase in temperature of a given mass of gas increases the number of gas molecules 
      b. An increase in the temperature of the gas does not affect the kinetic energy
      c. An increase in the pressure of the gas is directly proportional to the increase in the volume
      d. A decrease in the pressure of the gas is proportional to the increase  in volume at constant temperature
      e. A decrease in the pressure of the gas decreases the number of gas molecules
      ""","""36. """]

    question2= [Question(question_prompt2[0], "D"),
                Question(question_prompt2[1], "D"),
                Question(question_prompt2[2], "C"),
                Question(question_prompt2[3], "E"),
                Question(question_prompt2[4], 'A'),
                Question(question_prompt2[5], "C"),
                Question(question_prompt2[6], "C"),
                Question(question_prompt2[7], "D"),
                Question(question_prompt2[8], "A"),
                Question(question_prompt2[9], "D"),
                Question(question_prompt2[10], "C"),
                Question(question_prompt2[11], "B"),
                Question(question_prompt2[12], "D"),
                Question(question_prompt2[13], "A"),
                Question(question_prompt2[14], "C"),
                Question(question_prompt2[15], "D"),
                Question(question_prompt2[16], "D"),
                Question(question_prompt2[17], "E"),
                Question(question_prompt2[18], "C"),
                Question(question_prompt2[19], "C"),
                Question(question_prompt2[20], "D"),
                Question(question_prompt2[21], "C"),
                Question(question_prompt2[22], "E"),
                Question(question_prompt2[23], "E"),
                Question(question_prompt2[24], "C"),
                Question(question_prompt2[25], "B"),
                Question(question_prompt2[26], "C"),
                Question(question_prompt2[27], "D"),
                Question(question_prompt2[28], "D"),
                Question(question_prompt2[29], "B"),
                Question(question_prompt2[30], "D"),
                Question(question_prompt2[31], "C"),
                Question(question_prompt2[32], "E"),
                Question(question_prompt2[33], "D")]
    def run_test(questions):
        score=0
        for question in questions:
            answer=input(question.prompt)
            if answer.upper()==question.answer:
                print("Corrrect.Yeah! you got it that's the spirit. Keep it up\n\n")
                score+=2
            else:
                print("Wrong, the answer is",question.answer,"Awwn! maybe you will have luck in the next one\n\n")
        percent = str((score) //(len(questions * 2)) * 100)+"%"
        print("You got " + percent + " correct")
    run_test(question2)
def chemistry_year_1980():
    question_prompt3=["""
    1. In an attempt to remove sugar from a beaker containing a quantity of sand and sugar
    and sugar, 2m ammonium chloride solution was accidentally added instead of water. Which of the following 
    methods could be used to remove the ammonium chloride from the mixture
    a. Fractional distillation 
    b. Crystallization
    c. Filtration followed by evaporation
    d. Evaporation followed by sublimation
    e. Filtration followed by sublimation
    ""","""
    2. The alloy duralumin is used for the building of aeroplanes because it
    a. absorbs heat readily from the sun thereby preventing the inside of the plane from getting too cold at high altitudes
    b. reflects sunlight readily, thereby keeping the inside of the plane cool
    c. is extremely durable and possesses reflective ability 
    d. is easily the lightest building material 
    e. possesses both strength and lightness
    ""","""
    3. A solution X on mixing with AgNO₃ solution, gives a white precipitate soluble in NH₃. A solution Y, when
    added to X, also gives a white precipitate which is soluble on boiling. Solution Y contains 
    a. Ag+ ion
    b. Pb2+ ion
    c. Pb4+ ion
    d. Zn2+ ion
     e. Al3+ ion
     ""","""
     4. 10cm³ of CO is mixed and sparked with 100cm of air containing 21% O₂ . If all the volumes are measured at S.T.P
      the volume of resulting gases would be
      a. 90cm³
      b. 100cm³
      c. 105cm³
      d. 110cm³
      e. 115cm³
      ""","""
      5. A sample of an oxide of mercury weighed 1.00g. When this was heated, oxygen was given off, and 1.00g of
      mercury metal only was left. What is the formula oxide ?
      a. Hg₂
      b.HgO₂
      c. HgO₄
      d. HgO
      e. None of the above
      ""","""
      6. On heating under suitable conditions 1 litre of a monoatomic gas X, combines with 1½ litres of oxygen
      from an oxide. What is the formula of the oxide?
      a. XO₃
      b. X₂O₃
      c. X₃O₂
      d. XO₂
      e. None of the above
      ""","""
      7. If 1 litre of 2.2 M of sulphuric acid is poured into a bucket containing 10 litres of water, and the resulting solution ,mixed
      thoroughly, the resulting sulphuric acid concentration will be
       a. 2.2M
       b. 1.1 M
       c. 0.22 M
       d. 0.11 M
       e. 0.20 M
       ""","""
       8. 1.0g of 7CaCO was treated with excess 0.1M HCl. At the end og the reaction, the acid still left unreacted required 25cm
       of 0.1M NaCO to neutralise it. What is the original volume of the acid? (Na=23,Ca=40, C=12, O=16, Cl=35.5)
       a.220cm
       b.  """]
    question3 = [Question(question_prompt3[0], "D"),
                 Question(question_prompt3[1], "D"),
                 Question(question_prompt3[2], "C"),
                 Question(question_prompt3[3], "E"),
                 Question(question_prompt3[4], 'A'),
                 Question(question_prompt3[5], "A"),
                 Question(question_prompt3[6], "A"),]

    def run_test(questions):
        score=0
        for question in questions:
            answer=input(question.prompt)
            if answer.upper()==question.answer:
                print("Corrrect.Yeah! you got it that's the spirit. Keep it up\n\n")
                score+=2
            else:
                print("Wrong, the answer is",question.answer.upper(),"Awwn! maybe you will have luck in the next one\n\n")
        percent=str((score)/(len(questions*2))*100)+"%"
        print("You got "+percent+" correct")
    run_test(question3)
