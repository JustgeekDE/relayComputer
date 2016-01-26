*//////////////////////////////////////////////////////////
* Basic Relay using to voltage controlled switches
*//////////////////////////////////////////////////////////
*
* connections:      Normally open terminal
*                   |   Center terminal
*                   |   |   normally closed terminal
*                   |   |   |   positive supply
*                   |   |   |   |   negative supply
*                   |   |   |   |   |
*                   |   |   |   |   |
.subckt basicRelay  1   2   3   4   5

SOpen 1 center 4 5 SW_OPEN on
SClosed center 3 4 5 SW_CLOSED on

.model SW_OPEN SW(Ron=.1 Roff=1Meg Vt=6 )
.model SW_CLOSED SW(Ron=1Meg Roff=.1 Vt=6 )
.ends
