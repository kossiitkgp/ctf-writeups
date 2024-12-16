import sympy as sp
from Crypto.Util.number import *

ct = [3686831934110700898120939649143828123411410271994017685866712053479630491543721010218672046916737814750867256119026760272149723645263441900478932337215508840648452420798724789061099105201437816747052929007489792452271579250461205659384245400644343811235017294672130133467345421546011209355333514793842609086453, 1890160481037182252123817226487139003161916202370729077793798929447441285259601272007131239316526811117946321936239625109936311931913923482226040913356436736330671405790900091043968582088667762641533600351897406129427802004919260008711096006091596947487583067990271196950007080237764358004687294509200560768848, 530614740969558668515657666765423726168760348676389585149412070843400562157680641927864939209350909892289109242307257998368968627423229201715999911280269968680262454743648463730236602403152174170687974244552795279137291592035424989777630244328267982844083970866418576300359114667726370729840439101053941717628788, 114974190392900760213877770061084281834667105353808175453233389051691460056227503219747797376459004596052266162034090470202234448107038903876646414612324760231566930546381239712857427923395708793809318796741291908023927288500898126979114707823363374183061704340117475008755380981658030117251776574208697715996915877, 64957068505201945426702245769865626113605815863132381097995465824327776203713245107374657453073719186912459044157375742147048433448605716517761526321035014609019462168272663501829399246330461448798122037985769487185606556141323320534628765931670748833465621648824425034123860430532570298547817912425792159241915038, 11970333619208861261805624398426593494373020761158903447986501566929448240440057522492928099296014039174685007962969347168654534321334754668336024985392788026739313906825173958712483215262033133667851838905811082264176929165036201292337922414711125159460522332737101305040176733922143363108104011119057202287707, 257905779522858317389312487097804808510501519441361437406984895677297461792136482327309986956630255749109209240200837081950573982095353903942623718157803640049558450786935861071138069935620534338430735780746799439064190530192424150764051610709530016448240534506877799545151388488286477890309940681947909279231850, 93083001481108253541896682717913337294214063943106943407062628782407983943700543398688235542651644350143186005555736077311945112886380133323209178892019038079309716894021342886572470080601530424775485792545447095032383269255053686181982274967493344175902777541345701969472672920274207464727963710245786606638450024, 2069020026558375139989637499665737319283282943764057404209925207957017262791806778111323830229694738801288048565079313246396631908451228554594860029245889517068643479113447667078751436831384140852440274854491440942387858923950857602191914894319004099690381617982799849520381856057018964965971638327419687486679613, 18661195123467541569372180630881777845046490508784639540506321002148003860521252645741639280798157445030331915990926946956186024095058679755914849259806472720315915316764045049652804536031795842430906436421672136142594597651060862135794656080551278808753004919948021945345083906147187103242634427486389224988232, 7062201560880202019802324385609842299472580687038007842431603015806806858200749631862542626625076151007061427228470661094645341975594860924075906911548665136252824186481354504561026478583751172049653854357750028113987109356849337787032498691718911697408822573042758223370187343215879113596974567359887196113313, 164170122163742335036119284012927827867336805635929603624874641299469146265100812891978251675546839740135560404963824696360312058643319824230726691324103547139730082168464503696903531185078400998471467342818937192834443197023098553937243439104844445080047891419070458325718246162354007769267581207015793196345843, 4813409539215287746917542795481446331527117332678035671917434710781732273803749211297275978791391995561622276325113140851530258901943542796456847371869750498372507224291011786622453661226332373588596021574002394296705840943316492250044181016264055526368389447927511078827055904552539768892447887077203389687450851, 2472453272543113838449042005607533778665651657378854276943202506828801713465331745722074481057072173828154671062043656061163234499944952302805778938065133004258713147936052578205537610915913276318318323610465398178511794138691089778685270183678222979284979569209749013705132310080315617316024242244119317127618936437, 72922963569537281718062478207771896088248055685562595123090597215864368341529559439100869289515050009617859258086612971311204012726592386051314320851376885525179433190979361317109265593056155083410228563756892338022392846981032572419283245386077445688601372262914046606660469897950313695529908107868506272357143, 40110976487230319553425930997113047822952906967544032999753814971717083555575121288510018703337836869406423742088436720341661315014353247717408718088831287031164459804461373725676895949836384542626956992025549235199782989574761824166062993205260750229931598846136188127927465975270199967857973172724583347758836953, 72478884647397803010599022681495056709294152016000746246072898471141774997070969917577642982016010681091937330235959892414796320259188787893483223624673221308893039134913394459569665070694362992766674438084397473128274856668397578154920422779897131740626349133603259567085215534082965928455200038361090462057730841, 10993544144870022544822358265208673378225507885470516448853557667219073035537491116881289904481329685253007694138052607748261828254717632245058228063892105041494629352804604265693316645611534594066842980284709462581402026464020351419113132593592060186450720458482678135663272890902426305676742081984825393942199432, 7795391353486253563571094089143648956954326208132425582584782345690989731391057349965956187828767892943071986024672047237886937555695576666816490741041747796147042958827223030351062760570097508359388930226101182104460444358917409481270577372875325231255710978260730023529020712471610920954671019598970905442952, 1847931371603500842064390266829587052585493336618466125455291813284460638110066726989822981413696009012477358755982129154947829460138326785110279923989976440985775431480604153590192698143116711384735131821898503409055527836032747861636536228154619859989497969722494808988610206582778668225963654132576521741649, 129266925843647844862720937845197036702273414152678634156915034468560929609725977401179778821737796902626404142759330702479618085270086376371542851525401711700363453615783837424390552049301474481304721222097637657033205383412403121785165523242079639273066621956569626646031562008138497524429957877589687232360800179, 2865557877330607927214414565791572746885575091972034999106050231708428567680909801321928652875417929615162433591870461949077192379589552166488284868941405025055095777153415012968984585127356397097442644486582785549564430958686364184634345807624743752249101604898802555392275360136865877147954846201213379576688424, 105997347551446621211359740897258833020925362666679061423112267909877237562462427351113534985837527175677941959683139630989718615982327250141442945501699342313055002820689661306233663855315016460976514826710867887966010764949217472376483134901747884445989477566507579064318262669872743918266244124216782932668702032, 5870059393450955128713075188422569381743954906720839308406398853335416386654642292731657558066617206457895195573677863484699150794983935512773675153918375275845571545159422868216234736327683894148230075119983245755712166246522056519918994346853399252942832169075005839039684707347879247572220889795019786361777, 80895535780095555077939586986094007029406589633099033523478078467646883247084178208968085137506665195605611948457907041670767158523974720414609870626941929734355719551477219275298083868701713027777806008548829845833927620667102736472684607159902539179861878010663341221352496962812056535262074176813761644855316926, 5878384588336462880943594118003723465673967892433806494952462077865961995684725517017512046046946021954534331956297188091131405076539460208533145911598513204122115352402241294184822504547864592376637953731976463991548799235992506933147222777844161641863187472610208445051042786655808730530195567785034761075647239, 2490258332803850626808606401393351894622813857971822395792623591753929990397750445814152307841442079440001594270497891809115595740004231102829232131931484865470749341806180655806252051750866318803554491375975349365263092442350656041700154429956588772612208686728954499700702869779193042126181403089038261782008, 7714465638667425311780750125238105974253168987203684516292153033958463907791442137188320285027671799089378251294915901510997484952944546891285119979283429771250357303957223706943337493800040443958631431627858056813197046762739511785822456429440884615734004118233122217525551382232422468176032972437968573525967430, 43447254361894151338115771923762019780546628603509760338577073349468896554161678645847216332090346335653143255836461291551196628287626439290847349044457197595464813449500082826222809044173156086924155977978594456809253860093733978570682564916316833782223585400342503399989315460188924330717393321936549483508190, 518343417802899678151353020298265374399288446093908377240092431222964155997279805248499704044163376992721159620886033057130502818596580934866601997055219135014884535570569982081650099941951281743714100192593128882773221978370570920940256883184918625433739182041159912205281094342233691500030626278602445816588540614, 2532303231157514144440001564679550959034459562782785666747581350629927720220370790594006830720383229680558182219492981347880197926183335089432456604767713098773301353947040255386142981278075211897171750344567284718261879064459164829975840727491186870554742498561304821465480242762059783046301398947945152434269, 61893523043699065691589441785584096978340762936595060957250758253504713940129909735997047560282394943086638476160727397230265028591514675415950693833103341617860286181997882057777817550331119756368323209391660302736365437857619938426378642869499022169552467357678180635316742901968807664038926508293335841992579, 9927627451916377804350049692334541937908242455297293226493771957135391121160683041799694044820851421442081795403772159000206218845856958654217441577096354614926931059754954676117416399129446061519582829523757235848230727968402559109184395775757653009162229484446587958687745253215729688773994077406913330640622, 613488474689394101364292849562450133988948117059852870705972341343678840517509710045405698883560374940683533991767092973413013288869381574400468231948877405706831301611854347560025136714667588616161302924889912014400424677762975857643958760919091814079573123499231691265298010582320851244449544307667967481444113, 66030005458954428591881157330426466397998535462265450242813712600034061324478233485949265505915471455114127355909073837718401722760841445546044439263243046927905857262510689104141035281750154629579869672646066362576238981521843950529143897107647509286177911702710720668491504268217315615317702985143526608489808291]
nlist = [4674993922645010675237838605300928930371722385542973410523148222764620039225922667786842142606447669714931849255664281248575001943997204150648740799275864091570821818237331341466317919761075895627123365077645475151901373237610778478299834694224282144311481298001772132695374007618512397253024601725668850598599, 6189228522489240559250611335100222207597766651446973876558943286987107505351526107651831566895955131192642207259405061288374347923684378211342837964069943275618546423067751811937818855741582965237308621491005337168741395634624075269903175814957518547027474704179463919291575741485216128362401890610067511519109, 543089975498850982951749099842045819194446903400328191397610205529502755172845528746433630267533075309323561340348717357684364886809817045470697396864469792819256646361976127006902092466648199814650549299409960528582442257675690514295919427977557823230365040483146696202948213487644979493462127505557584974210599, 999771670269075206168593042186931925619310600289561567259074928057044460981298586056645894845356089628660935711828456967321817993671988105487967649669062964828117904228220864789488670750114434016727413641282790964195381372706868595700112537380670534343715412210084875580772857927481612924939625487343240305499793479, 77038261178869312433848478866409525818583562818345267542659606760590870347400160833038433483073056816329848711527945932857816035459009231708187279017184089599962407865437439198517205296426866435926148693861994753386324714490606565681929170751096017824111724853273904566779540320690768826122281022579227570904936257, 50538558302476302313177270849162538319877129289458348625110204070860999195965478544462896063593067417391501444673317698597096646468864820163667730178994251199472544909179820266826652686681448661010229810838421776781924100063395706105207135888958849219435137343421227397197135090726793215992506529263384056699011, 533754748080443876533845775573958356136220514895303372061416668714594867894846336793892249925949450601414314267599077565142955897933114874310397680185575515554581541264226853140545552378289322452105090534720270686229832975581827200134269532807164540815524737348607475620913480964045015287061773267446664308596703, 174526994661906196319225668684054923222895353600272009142872816890027985791341291163044144922302102660373741880755902374676355231900749905692034205432542389967679179395047428822744943249229415242473156722718097469388583134100325305368955778508687989865649561794858293181806948292023417224339192014066003277203744301, 4738814280210021402601074858672087656179567091882082647346318137965594873798020946064227255911652074055858731713184910747533072909867343396967228594555018618615889430451533012000474675567004690587760982874659323133889173549341554956015125747924802029972028178158933865290617807485591327131194384633062451145998351, 19134681472346722888191721785190276356502768036439646394040320996665113362539930229437759467018516496476712972681462633035422504358820035914138291600114352636706514327489651186034887654063176879127694226118289563506752926637079853950879675610464799873066251038332181790220525248680414669984830305346267218863801, 48020293843689165024851496202336493823305022108306061731540617516502586138293543463666958381660316774820893911706140580181351216468615274426224459702271043339897180377749263707749005823935319229741397298482126229183986215327843642959397860272891229223136144253828532086133401443762122496061109425199349610197559, 174320097973654824350620775443701545200166604097774654232217133389479398149243115993735701512638340073407585439552369174606318088212871918804153054963311588107211610252916534118302786363045521130714872788657833441517250054572374902080769482933495186955299920005361266681552797181963682228181781561710387457253657, 10461518248805709604205515162268234326230762345671977504180598106791766959718192926338920979016629100572103907559293240143746391930070325970723442166078515634181156672807310040804512874508789629157416548102928582956485778201350748392462534946772611581124244099472983858883837612857846229767550624729339004515036611, 2891871211740169126076925648916644279896163653615105752401016358786803843201514601366555133890718871129546371847416766625033072552392946927330619841434412180389140070697147591868771281474952308721243221480778044777956576471541826359226548847474608359760742008065791847851173858421962845098307801046552049627596798531, 147678719666695156900043854430408123586383796136775541242624368906938090594384860257672248977210191451010816984633094963495607377165126227169360449895065888849164589143980952864200336902744121882357237398656097654460450808451452684560726944912565795169257337567580786434391278167300496155581951487747663530765283, 64168424990238915196533295527281143344591596868946630411239068450008703353550406233241188290761172209873096126697868422711619511217842269948961403984215418726758317215499714079058275920857633335908166568202933040859556657590001774991782074645331857054465391019071239815529778938867260118078457098750110394870463243, 99354463511331843052050865963938898206234306500192939079359730310445318674257331725180637084591040791210506882210633596883495806601699908232711946170634492346540846291281103787647532431738219979075946395839493130864880684452231410879191795404796220486902109649747628065831521121981802831830191495159914159369646137, 11319993891887875400526662543433001040102736323373974338738418820108966978610922939647708784719430091438825138779174850246421429276133395900716446414665276863491625165865965375885672264083490049935557636537362106899902425248470265435201673002237155515938986365365678855367647009443319239462795632688920797097717503, 228809820867599788189251660463414636713831669504410785632698347177569062693113272563446432127422629859897280075959520711267880041890300186061021934138300658692376119321846436753169655486099297267065819719050971198045237196412055821784835389357661081389555059389567994421467777780272991930931786818894827811900009, 2027960748040427369787185312780964638490776949586395312681783154931615769989303964559356439550927570062452924053318013689273471018926869746664047039193768587037656011708177925597518255127424630049586006549964800777488713360624742793827692171906944072944211101976784185009191348819385609427157924817224306795489, 513186834755413454016914911155217211725671252540300369110212670933002340418279224550853423402443957445584157998087419828115207697619631880981728138068227068683215916680680640182395341333563576104775488182264665061502114145512979379896179471353282130954873478747585873407406261662380983432342576295854083604516916757, 8611693708487675372410321284184360108188250917293107071103626828561741625983321734742737476198299345711668247223572148140711621931968130585421259915743170604301820836466375271757381915880735559410982132835784717533119634144983590740740790247210540101285753905827241343742224995891368783730493156059681565267705803, 246924856104481379414547861233062982921086210709356112548124074633948943175293969532934445023166664805687712085210813690937154687016332025945417152984813232672350926062785406447780564815727298030459168364616299042067978663509073511066428652003338422095511000667009816530457707556089371432844327206637696864642434841, 7327762728759722262713914488907614312078333207636315548831898220960118876640256221151081480577773800522145637057116155261010982338316953205168749659452309123950429790792478458267785049670248114689693801662682528180061643075417731624536541400765218156084725692206709926843133725557361242008340222939833689128267, 500295059559948078552275708518365865215286687611294703228075693579131344444475691404118115620073044529437003620518115878778648637895621379851276531247868196253440544469633674380053905943651826855620833288754383273916525327734797255204660028631414775038297548164424788850073595116049265024636944126722586105293186433, 13922669313450531978493561498858060069005581797718514312546316172742161742075140414705377331157503222643601407298180150662186325568693994697172885682322054838994765985557275372976290867675442635938224391462655388188822502111430204709230560318873051699484189664347928405125762178122476717847702564618868598950664683, 7656089504259816700452679794834447783263019306525594803462690424117675981051508045081077727054158317842630902553534360465177921105699405894478692257458538582981129427617356973233255378885046312822063971832113901408497344038750569652654075488813565642494491304503848498632682117553265883579598281868416041533979, 8587472369862340529564506963901027828608441165124278752241298895198831693040460158158435275792164254277238572039275469772666364376701688861864540645615828856737778317268490130154949945764730972978722049433659137196739691745273937666827729124857131061065482859716720587273036540381225119550601945484312784547710113, 231208411808783585322218105695396735982378900001100972362612418773818932581479268568125615206969598353721082039194057162584873504467811379593934813543042028449332967940268729108418710826180835142776358826458920351784275844028873110962582246831184233109230508493861607472908409069894132788659824712694251032691961, 3950844678925735519411786322704182145546814734642685908706155694953728564730398693211954317285389708797566541037218887296798836383185618924366483502692581901263891698768138174244181714520197003213321680488631876251597538446449062412042820713300397867391919732010496346930672337692800551661295664551658160723798516679, 5273299491448494392193094648902643211496881772312515437638957839052554904492689968401176843251431847691756146283548494149081365578671530805799739958855050121075485844319151226983159869329668644510591703276278555645634718190562811231123161463499793607033127173388939587495161824996165989274923493445280404780399, 76445681568331020621344046334086198313824514277978437647713088513440916494632693468308387002607895403303250476686285594528090682060787703498043005479288670514931456185319394390520201824377064668912502787965043193181208377218087161691223889789351157003940437095884255174276782003966074215283723292255435337773577, 39462386043941438396179504608189523110572237407487996164639623297588372450211816950965596388072112536164887505902199009486540094527681887195125096595609767415060919571678535813300076517554167327256619683065115271050709558726034652192371188795244229421076711113648583951057223277767294928904932505456609319795909, 683357923869887606763683860170705484024447169857951426138705665893388720575818231818847232596836841340533621015479330651670362690186813285641171640129663787748126071145084372823696287802708394342196670388177046913091990188529895967556924023940927084513817145114651124816723773948752725933420631051127831674849537, 301278612058304538593331063909019148485116953335292463523154770478637810468089476003571216309836864341901283817293480800414830762828951144354823739781812043104518553365706013075789737157901216030247531145906274591900783890597646572455211822951679371809716857248718005056719390246899815370394152917418421943987111433]

language = {
    'A': 'Α', 'a': 'α',
    'B': 'Β', 'b': 'β',
    'C': 'Σ', 'c': 'σ',
    'D': 'Δ', 'd': 'δ',
    'E': 'Ε', 'e': 'ε',
    'F': 'Φ', 'f': 'φ',
    'G': 'Γ', 'g': 'γ',
    'H': 'Η', 'h': 'η',
    'I': 'Ι', 'i': 'ι',
    'J': 'Ξ', 'j': 'ξ',
    'K': 'Κ', 'k': 'κ',
    'L': 'Λ', 'l': 'λ',
    'M': 'Μ', 'm': 'μ',
    'N': 'Ν', 'n': 'ν',
    'O': 'Ο', 'o': 'ο',
    'P': 'Π', 'p': 'π',
    'Q': 'Θ', 'q': 'θ',
    'R': 'Ρ', 'r': 'ρ',
    'S': 'Σ', 's': 'ς',  
    'T': 'Τ', 't': 'τ',
    'U': 'Υ', 'u': 'υ',
    'V': 'Ω', 'v': 'ω',
    'W': 'Ψ', 'w': 'ψ',
    'X': 'Χ', 'x': 'χ',
    'Y': 'Υ', 'y': 'υ',
    'Z': 'Ζ', 'z': 'ζ'
}

reversed_language = {
    'Α': 'A', 'α': 'a',
    'Β': 'B', 'β': 'b',
    'Σ': 'C', 'σ': 'c',
    'Δ': 'D', 'δ': 'd',
    'Ε': 'E', 'ε': 'e',
    'Φ': 'F', 'φ': 'f',
    'Γ': 'G', 'γ': 'g',
    'Η': 'H', 'η': 'h',
    'Ι': 'I', 'ι': 'i',
    'Ξ': 'J', 'ξ': 'j',
    'Κ': 'K', 'κ': 'k',
    'Λ': 'L', 'λ': 'l',
    'Μ': 'M', 'μ': 'm',
    'Ν': 'N', 'ν': 'n',
    'Ο': 'O', 'ο': 'o',
    'Π': 'P', 'π': 'p',
    'Θ': 'Q', 'θ': 'q',
    'Ρ': 'R', 'ρ': 'r',
    'Σ': 'S', 'ς': 's',  
    'Τ': 'T', 'τ': 't',
    'Υ': 'U', 'υ': 'u',
    'Ω': 'V', 'ω': 'v',
    'Ψ': 'W', 'ψ': 'w',
    'Χ': 'X', 'χ': 'x',
    'Υ': 'Y', 'υ': 'y',
    'Ζ': 'Z', 'ζ': 'z'
}

def googly(number, position):
    mask = 1 << position
    return number ^ mask

def string_to_int(message):
    return int.from_bytes(message.encode('utf-8'), byteorder='big')

def int_to_string(number):
    return number.to_bytes((number.bit_length() + 7) // 8, byteorder='big').decode('utf-8')

def reverse_alphabet(char):
    if(char=='e'):
        return '_'
    elif char.isupper():  
        return chr(155 - ord(char))  
    elif char.islower():  
        return chr(219 - ord(char)) 

out = "mrgπeτfΟΔςoΝeηiδyegsλexlwVαehιΠπμZe" # 35 characters
flag = ""

for i in range(0, 35):
    if out[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        flag += reverse_alphabet(out[i])
    else:
        eng = reversed_language.get(out[i])
        ct[i] = googly(ct[i], ct[i].bit_length() - ord(eng))
        p, q = sp.factorint(nlist[i])
        phi_n = (p-1)*(q-1)
        e = 65537
        d = sp.mod_inverse(e, phi_n)
        dec = pow(ct[i], d, nlist[i])
        flag += int_to_string(dec)

first_ = flag.find('_')
last_ = flag.rfind('_')

flag = flag[:first_] + '{' + flag[first_ + 1:last_] + '}'

print(flag)
