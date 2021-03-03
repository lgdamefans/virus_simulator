def economical_change(population,Config):
    '''
    five economical factor are considered : People Houses Business Govern Healthcare
    Parameters
    ----------
    population
    Config

    Returns
    -------

    '''

    personalgdp = 2500.0
    employmentrate = 1;
    basicbsgdp = 15000000.0
    infection_rate = len(population[population[:,6] == 1])/len(population)
    # as the infection rate rise, the business is shuting down
    phealnum = len(population[population[:,6] == 0])
    pimmune = len(population[population[:,6] == 2])
    peoplegdp = (phealnum+pimmune) * personalgdp*(0.5+0.5*(1-infection_rate))
    if infection_rate < Config.lockdown_percentage:
        businessgdp = basicbsgdp*(0.6*(1-infection_rate/Config.lockdown_percentage)+0.4)
    else:
        businessgdp = basicbsgdp*0.4
    governgdp = 0.15*peoplegdp + 0.25 * businessgdp
    totalgdp = peoplegdp + governgdp + businessgdp
    return peoplegdp,businessgdp,governgdp,totalgdp

