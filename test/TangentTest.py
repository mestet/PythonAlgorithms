import time
from decimal import Decimal

from mgu import Tangent


def test():
    test_cases = (
        ('50', '7', '1.000000'),
        ('99', '7', '63.65674'),
        ('1', '7', '0.01570926'),
        ('50', '20', '1.0000000000000000000'),
        ('25', '50', '0.41421356237309504880168872420969807856967187537695'),
        ('75', '100', '2.414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641573'),
        ('66', '200', '1.6909076557850112467449227568864597401394020064505316353407207088917011690795872240713734218879172646327770160651725652050484859618219879697752051810951362904457753202511784197236383032272382562934373'),
        ('33', '400', '0.5703899296732948869842944367165171344395916612277803588670767321648773185785139182667281174457178562297893243008142072872853286888960328100690865086908251916306044433718985107873049499896410747651198277527226796299574297144599467662451565824991733541829662982017242298421333390256456774571988988757135105640889382555549825129116125791099733839132220781770885074880665542087613574365108673861349851358'),
        ('10', '800', '0.15838444032453629383888309269436641143391621607373329723174099503565763714271398095982068671167683969760247784246245635360127468503585854989072371641780945676015630068842448679324654631180455508244681609912246894682999767163889608954348200513261457383402631956207134135845717820362730291944486457035414363730562482687040853346672445464025286723412132546155552811698994184624121727344889694851792286232241133395607343200411748478309419515767807983289586358336731727642054115831993793775656871279882490021287166738586276120493965644666856439651058308068286450386708601676856508970364709197647311234308440977758827880942092629113982645586313580967666947060720097442459050573743643629348352831544764243711614623496828980899971296580153167078839651266607025572214895991348656470848812029204324517464990712'),
        ('1', '1000', '0.01570925532366491632332444685471429414590278505146389224174147024125513603616290825876930402977752147061234884400926747946442337921935079864528657098293176018299949673806065643036899788340828285819506613607992292470118177247430096163586239307691371371704944465670402163900001411199392045544681926180494746369471838461759245035648437765821119403838769497784552028432479718963988161732804774611140953884197552669195663545939836517679565757794982392910647925895575281874835436230309593983924264745699193750954057603990655015977427796061183071416028534375645476591739962723230688018474829480417560610303836082632106053057215921602636321139866662095324238090165176472552645345238589026643300927215420651546741915016060747010427006361356973717073154657546886467069281626168030884563348549625830771569837919670741244095865551397581674575249713456440086151601514471924025175058065437744099347842595355113095166686392752519206987507226488533870825462805210706262891688719475558706314365606020395887690114610419'),
    )

    for tc in test_cases:
        start_ns = time.time_ns()
        actual = Tangent.tangent(tc[0], int(tc[1]))
        elapsed_ns = (time.time_ns() - start_ns) // 1_000_000
        expected = Decimal(tc[2])
        verdict = "Passed" if actual == expected else "Failed"
        print(f'Test {verdict}: ang: {tc[0]}, precision: {tc[1]}, elapsed: {elapsed_ns} ms')
        print(f'Expecting result:\n{expected}')
        print(f'Actual result:\n{actual}')
        print('='*120)


if __name__ == '__main__':
    test()