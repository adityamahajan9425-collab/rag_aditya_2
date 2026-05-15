"""
Space Missions Knowledge Base
Curated data from ISRO and NASA mission reports
"""

MISSIONS = [
    # ─── ISRO MISSIONS ───────────────────────────────────────────────────────
    {
        "id": "isro_chandrayaan1",
        "title": "Chandrayaan-1 | ISRO Lunar Mission",
        "agency": "ISRO",
        "type": "Lunar Orbiter",
        "launch_date": "October 22, 2008",
        "end_date": "August 28, 2009",
        "status": "Completed",
        "content": """
Chandrayaan-1 was India's first lunar probe launched by ISRO on October 22, 2008, 
from the Satish Dhawan Space Centre using a PSLV-C11 rocket. The spacecraft was 
inserted into lunar orbit on November 8, 2008.

Mission Objectives:
- Prepare a three-dimensional atlas of the Moon
- Conduct chemical and mineralogical mapping of the lunar surface
- Search for evidence of water ice near the polar regions

Key Instruments:
- Moon Mineralogy Mapper (M3) – NASA-provided instrument
- Terrain Mapping Camera (TMC)
- HyperSpectral Imager (HySI)
- Lunar Laser Ranging Instrument (LLRI)
- Mini-SAR (NASA instrument for water-ice detection)
- CIXS (Chandrayaan-1 X-ray Spectrometer)

Major Discovery:
The M3 instrument on Chandrayaan-1 confirmed the presence of water molecules 
on the lunar surface in 2009. This was a landmark discovery in lunar science, 
later verified by multiple independent analyses. The spacecraft impacted an 
impactor (Moon Impact Probe) on the lunar south pole on November 14, 2008, 
making India the fourth country to plant its flag on the Moon.

Timeline:
- Oct 22, 2008: Launch
- Nov 8, 2008: Lunar orbit insertion
- Nov 14, 2008: Moon Impact Probe released
- May 2009: Orbit lowered to 200 km
- Aug 28, 2009: Communication lost; mission ended
- Total operational period: 312 days

Outcomes:
The mission discovered over 70,000 images and confirmed water/hydroxyl presence 
near polar regions. It operated for 312 days against a planned 2-year mission, 
due to premature loss of communication.
""",
        "tags": ["lunar", "water discovery", "moon", "orbiter", "PSLV"],
    },
    {
        "id": "isro_chandrayaan2",
        "title": "Chandrayaan-2 | ISRO Second Lunar Mission",
        "agency": "ISRO",
        "type": "Lunar Orbiter + Lander + Rover",
        "launch_date": "July 22, 2019",
        "end_date": "Orbiter active (2024+)",
        "status": "Partially Successful",
        "content": """
Chandrayaan-2 was India's second lunar exploration mission, consisting of an 
orbiter, a lander (Vikram), and a rover (Pragyan). It was launched on July 22, 
2019 aboard a GSLV Mk III-M1 rocket.

Mission Objectives:
- Soft landing near the lunar south pole (first ever attempt by any nation)
- Study lunar surface and subsurface for water ice and minerals
- Measure seismic activity of the Moon
- Map lunar exosphere

Spacecraft Components:
1. Orbiter (2,379 kg): 8 scientific payloads, remains operational
2. Vikram Lander (1,471 kg): Carried Pragyan rover
3. Pragyan Rover (27 kg): 6-wheeled robot with spectrometers

Key Instruments (Orbiter):
- Dual Frequency Synthetic Aperture Radar (DFSAR)
- Imaging IR Spectrometer (IIRS)
- Terrain Mapping Camera-2 (TMC-2)
- Chandrayaan-2 Large Area Soft X-ray Spectrometer (CLASS)
- Solar X-Ray Monitor (XSM)

Lander Crash:
On September 7, 2019, Vikram lander deviated from its intended trajectory 
during powered descent at approximately 2.1 km altitude due to a software anomaly 
in velocity braking. The lander hard-landed, ending communication.

Orbiter Success:
Despite the lander failure, the orbiter continues to function and has returned 
highly valuable data. As of 2024, the orbiter has been mapping the Moon continuously 
for over 4 years. It detected the solar corona during solar eclipses and provided 
the most detailed map of lunar south polar craters.

Timeline:
- Jul 22, 2019: Launch (GSLV Mk III)
- Aug 20, 2019: Lunar orbit insertion
- Sep 2, 2019: Lander separated
- Sep 7, 2019: Lander crash-landed (communication lost at 2.1 km)
- Orbiter: Still operational as of 2024

Legacy:
ISRO's Chandrayaan-2 orbiter carries CLASS instrument which detected sodium atoms 
in lunar exosphere for the first time. The mission paved the way for Chandrayaan-3.
""",
        "tags": ["lunar", "south pole", "lander", "rover", "GSLV", "Vikram", "Pragyan"],
    },
    {
        "id": "isro_chandrayaan3",
        "title": "Chandrayaan-3 | India's Successful Moon Landing",
        "agency": "ISRO",
        "type": "Lunar Lander + Rover",
        "launch_date": "July 14, 2023",
        "end_date": "September 2023",
        "status": "Successful",
        "content": """
Chandrayaan-3 was ISRO's third lunar mission and India's landmark achievement — 
becoming the FIRST nation to land near the lunar south pole and the FOURTH nation 
to achieve a soft lunar landing. It was launched on July 14, 2023.

Mission Objectives:
- Demonstrate safe and soft landing on the Moon
- Demonstrate rover roving on the Moon
- Conduct in-situ scientific experiments

Spacecraft Components:
1. Propulsion Module (2,148 kg): Carries SHAPE instrument; stayed in lunar orbit
2. Vikram Lander (1,752 kg): Successfully soft-landed
3. Pragyan Rover (26 kg): Traversed ~100 meters of lunar surface

Scientific Instruments:
Lander (Vikram):
- RAMBHA-LP: Langmuir Probe for plasma density
- ChaSTE: Thermal conductivity/temperature probe (confirmed 70°C surface temp drop)
- ILSA: Seismic activity detector (recorded lunar "moonquakes")
- LRA: Laser Retroreflector Array (NASA instrument)

Rover (Pragyan):
- APXS: Alpha Particle X-ray Spectrometer (confirmed sulphur, iron, calcium, oxygen)
- LIBS: Laser Induced Breakdown Spectroscope

Landing and Surface Operations:
On August 23, 2023, at 18:04 IST, Vikram lander touched down at 69.37°S, 32.35°E 
near the lunar south pole — a feat never achieved before. Pragyan rover rolled out 
and confirmed the presence of sulphur, aluminium, calcium, iron, chromium, 
titanium, manganese, silicon, and oxygen in the lunar regolith.

ChaSTE data revealed a 70°C temperature difference between the surface (50°C) 
and subsurface (-10°C at 80mm depth), crucial for understanding lunar thermal properties.

Timeline:
- Jul 14, 2023: Launch (LVM3-M4)
- Aug 5, 2023: Lunar orbit insertion
- Aug 17, 2023: Lander separation
- Aug 23, 2023: Successful soft landing (18:04 IST)
- Aug 24–Sep 2, 2023: Rover operations (one lunar day = 14 Earth days)
- Sep 4, 2023: Lander and rover put to sleep for lunar night
- Mission status: Lander/rover did not wake after lunar night (expected)

Historic Achievement:
India became the 4th nation after US, USSR, and China to achieve a soft lunar 
landing, and the FIRST to land near the lunar south pole. The mission cost 
approximately ₹615 crore (~$75 million) — remarkably cost-effective by global standards.
""",
        "tags": ["lunar", "south pole", "landing", "rover", "sulphur", "historic"],
    },
    {
        "id": "isro_mangalyaan",
        "title": "Mars Orbiter Mission (Mangalyaan) | ISRO",
        "agency": "ISRO",
        "type": "Mars Orbiter",
        "launch_date": "November 5, 2013",
        "end_date": "October 2022",
        "status": "Completed",
        "content": """
Mangalyaan (Mars Orbiter Mission, MOM) was India's first interplanetary mission, 
launched on November 5, 2013. It made India the first Asian nation and the fourth 
space agency to reach Martian orbit — achieved on the FIRST attempt.

Mission Objectives:
- Develop technologies for designing, planning, and managing an interplanetary mission
- Explore Mars surface features, morphology, mineralogy, and Martian atmosphere
- Study Martian methane and water vapor

Spacecraft: 1,337 kg total; 15 kg of scientific payload
Budget: ₹450 crore (~$74 million) — cheapest Mars mission in history at launch

Scientific Instruments:
1. Mars Color Camera (MCC): Captured iconic images including the Olympus Mons 
   and Valles Marineris in full disk view
2. Thermal Infrared Imaging Spectrometer (TIS): Surface temperature and emissivity
3. Methane Sensor for Mars (MSM): Upper limit on methane (< 6–7 ppbv)
4. Mars Exospheric Neutral Composition Analyzer (MENCA): Neutral composition of exosphere
5. Lyman Alpha Photometer (LAP): Measured Deuterium/Hydrogen ratio

Key Findings:
- MCC captured highest-resolution images of Phobos (Martian moon)
- LAP measured D/H ratio, helping understand Mars' water loss history
- MENCA provided first-ever measurements of Martian exosphere by India
- MSM set tight upper bounds on atmospheric methane
- Captured full-disk images of Mars showing dust storms

Timeline:
- Nov 5, 2013: Launch from SDSC, Sriharikota
- Dec 1, 2013: Trans-Mars injection burn
- Sep 24, 2014: Mars orbit insertion (first attempt, first Asian nation!)
- 2014–2022: Science operations (~8 years vs planned 6 months)
- Oct 2022: Battery depleted; mission ended after 8 years

Legacy:
MOM exceeded its 6-month design life by over 7 years. The mission was produced 
in just 15 months from concept to launch, a record for planetary missions. 
Its success elevated ISRO's reputation globally and demonstrated India's 
capability for low-cost, high-impact space exploration.
""",
        "tags": ["Mars", "orbiter", "interplanetary", "first Asian Mars mission", "Mangalyaan"],
    },
    {
        "id": "isro_aditya_l1",
        "title": "Aditya-L1 | ISRO Solar Observatory",
        "agency": "ISRO",
        "type": "Solar Observatory",
        "launch_date": "September 2, 2023",
        "end_date": "Active",
        "status": "Active",
        "content": """
Aditya-L1 is India's first solar space observatory and the first Indian spacecraft 
to be placed in a halo orbit around Lagrange Point 1 (L1) of the Sun-Earth system, 
approximately 1.5 million km from Earth.

Mission Objectives:
- Study solar corona, chromosphere, and photosphere
- Monitor solar wind and its origin
- Understand solar flares and Coronal Mass Ejections (CMEs)
- Study space weather and its impact on Earth

Spacecraft: 1,475 kg; carries 7 scientific payloads
Launch Vehicle: PSLV-C57 (XL configuration)

Scientific Payloads:
1. VELC (Visible Emission Line Coronagraph): Continuous solar corona imaging — 
   will send ~1,440 images/day; developed by IIA Bengaluru
2. SUIT (Solar Ultraviolet Imaging Telescope): UV images of photosphere/chromosphere
3. SoLEXS (Solar Low Energy X-ray Spectrometer): Soft X-ray flare monitoring
4. HEL1OS (High Energy L1 Orbiting X-ray Spectrometer): Hard X-ray flares
5. ASPEX (Aditya Solar Wind Particle EXperiment): Solar wind protons/alphas
6. PAPA (Plasma Analyser Package for Aditya): Electrons and heavy ions
7. MAG (Advanced Tri-axial High Resolution Digital Magnetometers): Magnetic field

Lagrange Point 1 Advantage:
L1 is a gravitational balance point where the spacecraft can maintain a stable 
position relative to Earth with minimal fuel. It provides 24/7 unobstructed 
view of the Sun with no eclipses, crucial for continuous monitoring of solar activity.

Timeline:
- Sep 2, 2023: Launch
- Jan 6, 2024: Successfully inserted into L1 halo orbit (127 days journey)
- Jan 2024–present: Continuous solar science operations

First Science Results (2024):
- Detected multiple solar flares and CMEs
- VELC captured first coronagraph images
- SUIT captured UV images of sunspots and active regions
- Data helped predict space weather events affecting Earth satellites

Significance:
India joins the elite club of nations with a dedicated solar mission, alongside 
NASA's Solar Dynamics Observatory and ESA's SOHO. Aditya-L1 provides critical 
input for India's space weather prediction capabilities.
""",
        "tags": ["solar", "L1", "corona", "solar flares", "CME", "space weather"],
    },
    {
        "id": "isro_gaganyaan",
        "title": "Gaganyaan | India's Human Spaceflight Program",
        "agency": "ISRO",
        "type": "Human Spaceflight",
        "launch_date": "Planned 2026",
        "end_date": "Active",
        "status": "In Development",
        "content": """
Gaganyaan is India's first crewed orbital spacecraft program by ISRO, aimed at 
demonstrating India's human spaceflight capability and sending 3 astronauts 
(Gagannauts) to a 400 km Low Earth Orbit (LEO) for 3 days.

Mission Objectives:
- Launch a 3-member crew to 400 km LEO
- Sustain crew for 3 days
- Safe splashdown in the Bay of Bengal
- Establish India as the 4th nation with independent human spaceflight capability

Mission Architecture:
1. Crew Module (CM): Pressurized module for crew; dimensions ~3.7m dia
2. Service Module (SM): Propulsion and power
3. Crew Escape System (CES): Abort capability at any flight phase
4. Launch Vehicle: Human Rated LVM3 (HLVM3)

Crew Members (Selected Astronauts):
- Group Capt. Prashanth Balakrishnan Nair
- Group Capt. Ajit Krishnan
- Group Capt. Angad Pratap
- Wing Cdr. Shubhanshu Shukla (also scheduled for Axiom Space ISS mission)

Training: All four astronauts trained at Gagarin Cosmonaut Training Centre, Russia

Test Flights:
- TV-D1 (Abort Test, Oct 2023): Crew module escape test — SUCCESSFUL
- TV-D2: Second abort test (planned)
- G1 (Uncrewed): First uncrewed Gaganyaan mission (planned 2025)
- G2 (Uncrewed with Vyommitra robot): Humanoid robot test mission
- G3 (Crewed): First crewed mission (planned 2026–27)

Vyommitra:
A half-humanoid space robot developed by ISRO to fly on uncrewed Gaganyaan missions, 
monitor cabin systems, and simulate human activities. It can operate panel switches, 
respond to voice commands, and converse with ground stations.

Budget: Approximately ₹9,023 crore (~$1.1 billion)

Significance:
Success of Gaganyaan will make India only the 4th country after USA, Russia, 
and China to independently send humans to space. It will also enable India's 
participation in the proposed Bharatiya Antariksha Station (Indian Space Station) by 2035.
""",
        "tags": ["human spaceflight", "crewed", "LEO", "astronauts", "LVM3", "Vyommitra"],
    },

    # ─── NASA MISSIONS ────────────────────────────────────────────────────────
    {
        "id": "nasa_artemis",
        "title": "Artemis Program | NASA Moon to Mars",
        "agency": "NASA",
        "type": "Crewed Lunar Missions",
        "launch_date": "2022–ongoing",
        "end_date": "Active",
        "status": "Active",
        "content": """
NASA's Artemis program is the successor to Apollo, aiming to return humans to 
the Moon sustainably for the first time since 1972, and then use it as a 
stepping stone for crewed Mars missions.

Program Goals:
- Land the first woman and first person of color on the Moon
- Establish sustainable lunar presence by 2030
- Use the Moon as a proving ground for Mars missions
- Build Lunar Gateway (space station in lunar orbit)

Artemis I (November 2022):
- Uncrewed test flight of SLS + Orion spacecraft
- 25.5-day mission, traveled 1.3 million miles
- Achieved farthest distance from Earth for habitable spacecraft: 270,000 miles beyond Moon
- Orion reached 99.9% of re-entry velocity; heat shield tested at 5,000°F (2,760°C)
- Splashdown: December 11, 2022 — Mission SUCCESS

Artemis II (Planned 2026):
- First crewed Artemis flight; 4 astronauts
- 10-day lunar flyby (no landing)
- Crew: Reid Wiseman, Victor Glover, Christina Hammock Koch, Jeremy Hansen (CSA)

Artemis III (Planned 2027):
- First crewed Moon landing since Apollo 17 (1972)
- SpaceX Starship selected as Human Landing System (HLS)
- Landing near lunar south pole (Shackleton crater rim area)
- 2 crew members to surface for ~6.5 days

Space Launch System (SLS):
- Most powerful rocket ever built (Block 1: 8.8 million lbf thrust)
- Core stage: 212 feet tall; with Orion: 322 feet total
- Burns 733,000 gallons of propellant in ~8 minutes

Orion Spacecraft:
- Crew Module: 3.6 billion km total radiation tested
- European Service Module (ESM): Built by ESA/Airbus
- Life support: 4 crew for 21+ days

Lunar Gateway:
Mini space station in Near-Rectilinear Halo Orbit (NRHO) around Moon
- HALO module + PPE (Power and Propulsion Element)
- International partners: ESA, JAXA, CSA
- Launch of PPE+HALO: Planned 2025–26
""",
        "tags": ["Moon", "crewed", "SLS", "Orion", "lunar south pole", "Mars", "Artemis"],
    },
    {
        "id": "nasa_jwst",
        "title": "James Webb Space Telescope | NASA/ESA/CSA",
        "agency": "NASA",
        "type": "Space Telescope",
        "launch_date": "December 25, 2021",
        "end_date": "Active (10+ years)",
        "status": "Active",
        "content": """
The James Webb Space Telescope (JWST) is the most powerful space telescope ever 
built, a joint mission of NASA, ESA, and CSA. Launched on Christmas Day 2021, 
it operates from L2 Lagrange point, 1.5 million km from Earth.

Primary Science Goals:
1. First Light and Reionization: Observe universe's first stars and galaxies
2. Galaxy Assembly: Study galaxy formation and evolution
3. Star and Planet Formation: Observe stellar nurseries and protoplanetary disks
4. Planetary Systems: Study exoplanet atmospheres; search for biosignatures

Technical Specifications:
- Primary Mirror: 6.5 m diameter (18 hexagonal gold-plated beryllium segments)
- Wavelength: Infrared (0.6–28.5 microns)
- Location: Sun-Earth L2 point (1.5 million km from Earth)
- Sunshield: 5 layers of Kapton, tennis-court sized; keeps telescope at -233°C
- Total Cost: ~$10 billion
- Design Life: 10 years (fuel for 20+ years)

First Images (July 2022):
- SMACS 0723: Deepest infrared image of universe (4.6 billion years of light)
- Stephan's Quintet: 150 million pixel mosaic of 5 interacting galaxies
- Southern Ring Nebula: Dying star's gas shells in unprecedented detail
- Carina Nebula: "Cosmic Cliffs" — star-forming region, 7,600 light-years away
- WASP-96b Exoplanet spectrum: Water, CO2 confirmed in atmosphere

Major Discoveries (2022–2024):
- Detected CO2 in exoplanet WASP-39b atmosphere (first definitive detection)
- Observed galaxies just 300 million years after Big Bang (record-breakers)
- Found evidence for very early massive galaxies challenging formation models
- Imaged directly the exoplanet HH 212 and protostellar jets
- Detected dimethyl sulfide (potential biosignature) on exoplanet K2-18b (confirmed water)
- Observed Jupiter's aurorae and storms in infrared
- Confirmed detection of CO2, methane, water on K2-18b "Hycean world"

Deployment Timeline:
- Dec 25, 2021: Launch (Ariane 5, Kourou, French Guiana)
- Jan 8, 2022: Sunshield fully deployed
- Jan 24, 2022: Reached L2 orbit
- Jul 12, 2022: First science images released
- 2022–present: Full science operations
""",
        "tags": ["telescope", "infrared", "exoplanets", "L2", "deep space", "galaxies", "Big Bang"],
    },
    {
        "id": "nasa_perseverance",
        "title": "Mars 2020 Perseverance Rover | NASA",
        "agency": "NASA",
        "type": "Mars Rover",
        "launch_date": "July 30, 2020",
        "end_date": "Active",
        "status": "Active",
        "content": """
Perseverance is NASA's most advanced Mars rover, part of the Mars 2020 mission. 
It landed in Jezero Crater on February 18, 2021, and is actively searching for 
signs of ancient microbial life and collecting samples for future return to Earth.

Mission Objectives:
- Search for signs of ancient microbial life (astrobiology)
- Characterize Martian geology and past climate
- Collect and cache rock/regolith samples for Mars Sample Return
- Demonstrate oxygen production from CO2 (MOXIE)
- Test technology for future human missions

Spacecraft: 1,025 kg; 6 wheels; plutonium-powered (MMRTG)
Landing Site: Jezero Crater — ancient lake delta, 3.5 billion years old

Scientific Instruments:
- Mastcam-Z: Stereo zoom cameras (can zoom 3.7m at 100m distance)
- SuperCam: Laser spectrometer + microphone for rock composition
- PIXL: X-ray fluorescence for detailed mineralogy
- SHERLOC: UV Raman spectrometer for organics detection
- RIMFAX: Ground-penetrating radar (up to 10m depth)
- MEDA: Weather station (temperature, pressure, humidity, UV)
- MOXIE: Oxygen production from CO2 (demonstrated 122 minutes of O2 production)

Ingenuity Helicopter:
- First powered, controlled flight on another planet (April 19, 2021)
- 72 flights completed (operations ended Jan 2024 after rotor blade damage)
- Total flight distance: ~17 km; max altitude: 24 m
- Revolutionized planetary exploration concept

Major Achievements:
- Collected 23+ rock core samples (as of 2024) for Mars Sample Return
- Detected organic molecules in Wildcat Ridge sample (Jezero delta)
- MOXIE produced 122 grams of oxygen total across experiments
- Ingenuity completed 72 successful flights
- Captured audio of Mars: first sounds including dust devil, wind, laser zaps
- Identified ancient lake delta sediments as most promising for biosignatures

Sample Caching:
Perseverance is the first mission designed to cache samples for future retrieval. 
The Mars Sample Return mission (NASA + ESA) plans to collect these tubes and return 
them to Earth in the 2030s — the first-ever Mars sample return mission.

Timeline:
- Jul 30, 2020: Launch
- Feb 18, 2021: Landing (Jezero Crater) — "Seven Minutes of Terror"
- Apr 19, 2021: Ingenuity first flight
- Sep 2021: First rock sample drilled (Rochette)
- 2021–present: Active science operations
""",
        "tags": ["Mars", "rover", "astrobiology", "sample return", "Ingenuity", "Jezero", "life"],
    },
    {
        "id": "nasa_artemis1_detail",
        "title": "Artemis I Mission Details | SLS First Flight",
        "agency": "NASA",
        "type": "Uncrewed Lunar Mission",
        "launch_date": "November 16, 2022",
        "end_date": "December 11, 2022",
        "status": "Completed",
        "content": """
Artemis I was the inaugural mission of NASA's Space Launch System (SLS) and Orion 
spacecraft, serving as an uncrewed flight test to validate systems for future crewed 
lunar missions.

Mission Duration: 25.5 days
Total Distance: ~1.3 million miles (2.1 million km)
Key Milestone: Farthest a spacecraft designed for humans has traveled from Earth

Objectives:
- Validate SLS performance for crew-rated flight
- Test Orion's heat shield during 24,500 mph re-entry (fastest since Apollo)
- Demonstrate Lunar Distant Retrograde Orbit (LDRO)
- Deploy 10 CubeSats (secondary payloads)
- Certify ground systems at Kennedy Space Center

Flight Profile:
1. Launch: Nov 16, 2022, 01:47 EST from LC-39B, Kennedy Space Center
2. Translunar Injection: SLS upper stage (Interim Cryogenic Propulsion Stage)
3. Lunar Flyby: ~130 km above Moon surface (Nov 21)
4. Distant Retrograde Orbit: 70,000 km beyond Moon (record distance)
5. Return Flyby: Second lunar flyby (Dec 5)
6. Re-entry: 24,500 mph; heat shield reached 5,000°F
7. Splashdown: Dec 11, 2022 (11:40 EST), Pacific Ocean off Baja California

SLS Block 1 Performance:
- Total thrust at liftoff: 8.8 million lbf (exceeds Saturn V)
- Core stage engines: 4x RS-25 (Shuttle heritage)
- Solid Rocket Boosters: 2x SRBs (Shuttle heritage, enhanced)
- Upper stage: ICPS (Delta Cryogenic Second Stage)

Orion Spacecraft Performance:
- Heat shield: Largest ablative heat shield ever flown (5.03 m diameter)
- Max deceleration: ~4g during re-entry
- Communication: 13 antennas; used Deep Space Network
- Mannequins: Commander Moonikin Campos + 2 phantoms (Helga/Zohar) with radiation sensors

CubeSat Payloads:
- ArgoMoon (ASI): Photographed Orion + ICPS
- BioSentinel: First biological experiment beyond Earth's radiation belts since Apollo
- LunaH-Map: Lunar hydrogen mapping (communications issue)
- NEA Scout: Near-Earth asteroid solar sail (signal lost post-deployment)
- Team Miles, CU-E3, EQUULEUS (JAXA), and others

Mission Result: COMPLETE SUCCESS
All primary objectives met; SLS and Orion certified for crewed Artemis II mission.
""",
        "tags": ["SLS", "Orion", "lunar orbit", "heat shield", "test flight", "Artemis"],
    },
    {
        "id": "nasa_voyager",
        "title": "Voyager Program | Interstellar Space",
        "agency": "NASA",
        "type": "Planetary/Interstellar Probe",
        "launch_date": "1977",
        "end_date": "Active (Interstellar)",
        "status": "Active (45+ years)",
        "content": """
The Voyager program consists of two spacecraft — Voyager 1 and Voyager 2 — launched 
in 1977 that have become the most distant human-made objects and have entered 
interstellar space, the region beyond the Sun's heliosphere.

Voyager 1:
- Launch: September 5, 1977
- Distance from Sun (2024): ~24 billion km (161 AU)
- Entered interstellar space: August 25, 2012 (first human object to do so)
- Speed: ~17 km/s (38,000 mph)
- Communication signal travel time: ~22.5 hours one-way

Voyager 2:
- Launch: August 20, 1977 (earlier than V1 but slower trajectory)
- Distance from Sun (2024): ~20 billion km (133 AU)
- Entered interstellar space: November 5, 2018
- Only spacecraft to have flown by all four outer planets

Key Discoveries — Jupiter (1979):
- Active volcanoes on Io (first extraterrestrial volcanism ever discovered)
- Complex storm systems; detailed Great Red Spot imaging
- Thin ring system around Jupiter
- Moon Europa's icy surface suggesting subsurface ocean

Key Discoveries — Saturn (1980–81):
- Complex ring structure with thousands of ringlets
- Discovered several new moons
- Titan's thick nitrogen atmosphere (Voyager 2 confirmed)
- Spokes in Saturn's B ring

Key Discoveries — Uranus (Voyager 2, 1986):
- Discovered 10 new moons and 2 new rings
- Found Uranus rotates on its side (97.8° axial tilt)
- Miranda's unusual surface (giant canyon Verona Rupes)

Key Discoveries — Neptune (Voyager 2, 1989):
- Great Dark Spot (storm as large as Earth)
- Discovered moon Triton's geyser activity (nitrogen geysers)
- Found 6 new moons and complete ring system
- Confirmed Neptune's winds are fastest in solar system (~2,100 km/h)

Interstellar Science:
Both spacecraft now measure the interstellar medium — cosmic rays, magnetic fields, 
and plasma from other stars. Data shows the heliopause boundary is not a smooth 
surface but irregular. Voyager 1's instruments confirmed the density of interstellar 
plasma is ~40x greater than heliospheric plasma.

Power Status (2024):
Running on radioisotope thermoelectric generators (RTGs). Engineers have turned off 
non-essential systems to extend the mission. Expected to maintain communication until ~2025–2030.

Legacy:
Voyager missions completed the "Grand Tour" of outer planets, forever changing 
our understanding of the solar system. The Golden Record aboard each spacecraft 
carries sounds and images of Earth — a cosmic message in a bottle.
""",
        "tags": ["interstellar", "outer planets", "Jupiter", "Saturn", "Neptune", "Uranus", "deep space"],
    },
    {
        "id": "nasa_parker_solar",
        "title": "Parker Solar Probe | Touching the Sun",
        "agency": "NASA",
        "type": "Solar Probe",
        "launch_date": "August 12, 2018",
        "end_date": "Active",
        "status": "Active",
        "content": """
NASA's Parker Solar Probe is the fastest human-made object ever created and the 
first spacecraft to fly through the Sun's outer atmosphere (corona). Launched in 
2018, it has broken records for closest solar approach and highest speed.

Mission Objectives:
- Determine the structure and dynamics of the solar corona
- Understand how the solar wind is accelerated
- Determine mechanisms of high-energy particle acceleration
- Solve the "coronal heating problem" (corona is 300x hotter than surface)

Technical Specifications:
- Heat Shield (TPS): 11.43 cm thick carbon foam; withstands 1,377°C
- Solar panels: Water-cooled to prevent melting near Sun
- Size: 3m wide; 685 kg

Record-Breaking Achievements:
1. Closest Solar Approach (Dec 24, 2024): 6.1 million km from Sun's surface
   - Entered the solar corona itself (becoming first to "touch" the Sun)
   - Temperature outside spacecraft: ~1 million°C
2. Fastest Human-Made Object: ~690,000 km/h (192 km/s) at closest approach
3. First to fly through the corona: Documented solar wind origin regions

Science Findings:
- Discovered "switchbacks" — sudden reversals in solar wind magnetic field
- Found solar wind is accelerated closer to Sun than expected (below 10 solar radii)
- Identified coronal streamers and their fine structure
- Measured dust-free zone around Sun (between ~4–19 solar radii)
- Captured images of Venus clouds during gravity assist flybys
- First direct in-situ measurements of the outer corona

Venus Gravity Assists:
Parker uses 7 Venus flybys to gradually lower its orbit around the Sun:
- June 2020: Photographed Venusian nightside — revealed atmospheric features
- Multiple flybys through 2025 to tighten orbit for final perihelion passes

Mission Schedule:
- Final perihelion (closest approach): December 2024 — 6.1 million km (RECORD)
- Estimated end: Late 2025 when fuel depletes

Coronal Heating Problem:
The Sun's surface is ~5,500°C but its corona reaches 1–3 million°C. Parker's 
measurements inside the corona are helping solve why the outer atmosphere is so 
much hotter — likely due to Alfvén wave heating and magnetic reconnection events 
("nanoflares"). This has been one of the longest unsolved puzzles in astrophysics.
""",
        "tags": ["solar", "corona", "solar wind", "fastest spacecraft", "speed record", "Sun"],
    },
    {
        "id": "isro_pslv_legacy",
        "title": "PSLV Program | ISRO's Workhorse Rocket",
        "agency": "ISRO",
        "type": "Launch Vehicle Program",
        "launch_date": "1993–present",
        "end_date": "Active",
        "status": "Active",
        "content": """
The Polar Satellite Launch Vehicle (PSLV) is ISRO's most reliable and versatile 
launch vehicle, nicknamed the "workhorse of ISRO." It has a remarkable success 
record and has launched satellites for over 34 countries.

Variants:
- PSLV-G (Generic): Standard 4-stage configuration
- PSLV-CA (Core Alone): No strap-on boosters; lighter payloads
- PSLV-XL (Extra Large): 6 extended strap-on boosters; heaviest payloads
- PSLV-DL: 2 strap-on boosters
- PSLV-QL: 4 strap-on boosters

Technical Specifications (PSLV-XL):
- Height: 44 meters
- Liftoff mass: ~320 tonnes
- Payload to LEO: 3,800 kg
- Payload to SSO: 1,750 kg
- Stages: 4 (alternating solid-liquid propulsion)

Notable PSLV Missions:
1. PSLV-C11 (2008): Chandrayaan-1 — First Indian Moon mission
2. PSLV-C25 (2013): Mars Orbiter Mission (Mangalyaan)
3. PSLV-C37 (2017): 104 satellites in one launch — WORLD RECORD at the time
4. PSLV-C57 (2023): Aditya-L1 solar observatory
5. PSLV-C58 (2024): XPoSat (X-ray Polarimeter Satellite) — India's first black hole study mission

Record Launch (Feb 15, 2017 — PSLV-C37):
104 satellites in a single mission:
- Cartosat-2D (India's main payload)
- 101 foreign nano-satellites (88 from USA)
- 2 Indian nano-satellites
Duration: Total deployment in ~12 minutes

Commercial Success:
PSLV has launched satellites for USA, UK, Germany, France, Canada, Israel, Japan, 
Singapore, and many other nations through Antrix/NSIL, generating significant 
foreign exchange for India.

Reliability: 
As of 2024, PSLV has achieved 58 consecutive successful flights after one early 
failure (1993), making it one of the most reliable operational rockets in the world.
""",
        "tags": ["PSLV", "launch vehicle", "rocket", "104 satellites", "commercial", "workhorse"],
    },
]

def get_all_missions():
    return MISSIONS

def get_mission_by_id(mission_id):
    for m in MISSIONS:
        if m["id"] == mission_id:
            return m
    return None

def get_missions_by_agency(agency):
    return [m for m in MISSIONS if m["agency"].upper() == agency.upper()]
