def ecallayout(i, p, *rows): i[p] = DQMItem(layout=rows)

ecallayout(dqmitems, '00 Shift/Ecal/00 Summary',[{'path': 'EcalBarrel/EBSummaryClient/EB global summary', 'description': 'Summary of the data quality. A channel is red if it is red in any one of RawData, Integrity, Timing, TriggerPrimitives, and HotCells task. A cluster of bad towers in this plot will cause the ReportSummary for the FED to go to 0 in online DQM.'}],[{'path': 'EcalEndcap/EESummaryClient/EE global summary EE -', 'description': 'Summary of the data quality. A channel is red if it is red in any one of RawData, Integrity, Timing, TriggerPrimitives, and HotCells task. A cluster of bad towers in this plot will cause the ReportSummary for the FED to go to 0 in online DQM.'}, {'path': 'EcalEndcap/EESummaryClient/EE global summary EE +', 'description': 'Summary of the data quality. A channel is red if it is red in any one of RawData, Integrity, Timing, TriggerPrimitives, and HotCells task. A cluster of bad towers in this plot will cause the ReportSummary for the FED to go to 0 in online DQM.'}])
ecallayout(dqmitems, '00 Shift/Ecal/01 FE Status',[{'path': 'EcalBarrel/EBSummaryClient/EBSFT front-end status summary', 'description': 'Summary of the raw data (DCC and front-end) quality. A channel is red if it has nonzero events with FE status that is different from any of ENABLED, DISABLED, SUPPRESSED, FIFOFULL, FIFOFULL_L1ADESYNC, and FORCEDZS. A FED can also go red if its number of L1A desynchronization errors is greater than 1.0 * log10(total entries).'}],[{'path': 'EcalEndcap/EESummaryClient/EESFT EE - front-end status summary', 'description': 'Summary of the raw data (DCC and front-end) quality. A channel is red if it has nonzero events with FE status that is different from any of ENABLED, DISABLED, SUPPRESSED, FIFOFULL, FIFOFULL_L1ADESYNC, and FORCEDZS. A FED can also go red if its number of L1A desynchronization errors is greater than 1.0 * log10(total entries).'}, {'path': 'EcalEndcap/EESummaryClient/EESFT EE + front-end status summary', 'description': 'Summary of the raw data (DCC and front-end) quality. A channel is red if it has nonzero events with FE status that is different from any of ENABLED, DISABLED, SUPPRESSED, FIFOFULL, FIFOFULL_L1ADESYNC, and FORCEDZS. A FED can also go red if its number of L1A desynchronization errors is greater than 1.0 * log10(total entries).'}])
ecallayout(dqmitems, '00 Shift/Ecal/02 Integrity',[{'path': 'EcalBarrel/EBSummaryClient/EBIT integrity quality summary', 'description': 'Summary of the data integrity. A channel is red if more than 0.01 of its entries have integrity errors.'}],[{'path': 'EcalEndcap/EESummaryClient/EEIT EE - integrity quality summary', 'description': 'Summary of the data integrity. A channel is red if more than 0.01 of its entries have integrity errors.'}, {'path': 'EcalEndcap/EESummaryClient/EEIT EE + integrity quality summary', 'description': 'Summary of the data integrity. A channel is red if more than 0.01 of its entries have integrity errors.'}])
ecallayout(dqmitems, '00 Shift/Ecal/03 Occupancy',[{'path': 'EcalBarrel/EBOccupancyTask/EBOT digi occupancy', 'description': 'Digi occupancy.'}],[{'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -', 'description': 'Digi occupancy.'}, {'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +', 'description': 'Digi occupancy.'}])
ecallayout(dqmitems, '00 Shift/Ecal/04 Noise',[{'path': 'EcalBarrel/EBSummaryClient/EBPOT pedestal quality summary G12', 'description': 'Summary of the presample data quality. A channel is red if presample mean is off by 25.0 from 200.0 or RMS is greater than 3.0. RMS threshold is 6.0 in the forward region (|eta| > 2.1). Channels with entries less than 6 are not considered.'}],[{'path': 'EcalEndcap/EESummaryClient/EEPOT EE - pedestal quality summary G12', 'description': 'Summary of the presample data quality. A channel is red if presample mean is off by 25.0 from 200.0 or RMS is greater than 3.0. RMS threshold is 6.0 in the forward region (|eta| > 2.1). Channels with entries less than 6 are not considered.'}, {'path': 'EcalEndcap/EESummaryClient/EEPOT EE + pedestal quality summary G12', 'description': 'Summary of the presample data quality. A channel is red if presample mean is off by 25.0 from 200.0 or RMS is greater than 3.0. RMS threshold is 6.0 in the forward region (|eta| > 2.1). Channels with entries less than 6 are not considered.'}])
ecallayout(dqmitems, '00 Shift/Ecal/05 RecHit Energy',[{'path': 'EcalBarrel/EBSummaryClient/EBOT energy summary', 'description': '2D distribution of the mean rec hit energy.'}],[{'path': 'EcalEndcap/EESummaryClient/EEOT EE - energy summary', 'description': '2D distribution of the mean rec hit energy.'}, {'path': 'EcalEndcap/EESummaryClient/EEOT EE + energy summary', 'description': '2D distribution of the mean rec hit energy.'}])
ecallayout(dqmitems, '00 Shift/Ecal/06 Timing',[{'path': 'EcalBarrel/EBSummaryClient/EBTMT timing quality summary', 'description': 'Summary of the timing data quality. A 5x5 tower is red if the mean timing of the tower is off by more than 2.0 or RMS is greater than 6.0 (6.0 and 12.0 in forward region). Towers with total entries less than 15 are not subject to this evaluation. Since 5x5 tower timings are calculated with a tighter time-window than per-channel timings, a tower can additionally become red if its the sum of per-channel timing histogram entries is greater than per-tower histogram entries by factor 1.66666666667 (significant fraction of events fall outside the tight time-window).'}],[{'path': 'EcalEndcap/EESummaryClient/EETMT EE - timing quality summary', 'description': 'Summary of the timing data quality. A 5x5 tower is red if the mean timing of the tower is off by more than 2.0 or RMS is greater than 6.0 (6.0 and 12.0 in forward region). Towers with total entries less than 15 are not subject to this evaluation. Since 5x5 tower timings are calculated with a tighter time-window than per-channel timings, a tower can additionally become red if its the sum of per-channel timing histogram entries is greater than per-tower histogram entries by factor 1.66666666667 (significant fraction of events fall outside the tight time-window).'}, {'path': 'EcalEndcap/EESummaryClient/EETMT EE + timing quality summary', 'description': 'Summary of the timing data quality. A 5x5 tower is red if the mean timing of the tower is off by more than 2.0 or RMS is greater than 6.0 (6.0 and 12.0 in forward region). Towers with total entries less than 15 are not subject to this evaluation. Since 5x5 tower timings are calculated with a tighter time-window than per-channel timings, a tower can additionally become red if its the sum of per-channel timing histogram entries is greater than per-tower histogram entries by factor 1.66666666667 (significant fraction of events fall outside the tight time-window).'}])
ecallayout(dqmitems, '00 Shift/Ecal/07 TriggerPrimitives',[{'path': 'EcalBarrel/EBSummaryClient/EBTTT emulator error quality summary', 'description': 'Summary of emulator matching quality. A tower is red if the number of events with Et emulation error is greater than 0.1 of total events. Towers with entries less than 3 are not considered.'}],[{'path': 'EcalEndcap/EESummaryClient/EETTT EE - emulator error quality summary', 'description': 'Summary of emulator matching quality. A tower is red if the number of events with Et emulation error is greater than 0.1 of total events. Towers with entries less than 3 are not considered.'}, {'path': 'EcalEndcap/EESummaryClient/EETTT EE + emulator error quality summary', 'description': 'Summary of emulator matching quality. A tower is red if the number of events with Et emulation error is greater than 0.1 of total events. Towers with entries less than 3 are not considered.'}])
ecallayout(dqmitems, '00 Shift/Ecal/08 Hot Cells',[{'path': 'EcalBarrel/EBSummaryClient/EBOT hot cell quality summary', 'description': 'Summary of the hot cell monitor. A channel is red if it has more than 100.0 times more entries than phi-ring mean in either digi, rec hit (filtered), or TP digi (filtered). Channels with less than 20 entries are not considered. Channel names of the hot cells are available in (Top) / Ecal / Errors / HotCells.'}],[{'path': 'EcalEndcap/EESummaryClient/EEOT EE - hot cell quality summary', 'description': 'Summary of the hot cell monitor. A channel is red if it has more than 100.0 times more entries than phi-ring mean in either digi, rec hit (filtered), or TP digi (filtered). Channels with less than 20 entries are not considered. Channel names of the hot cells are available in (Top) / Ecal / Errors / HotCells.'}, {'path': 'EcalEndcap/EESummaryClient/EEOT EE + hot cell quality summary', 'description': 'Summary of the hot cell monitor. A channel is red if it has more than 100.0 times more entries than phi-ring mean in either digi, rec hit (filtered), or TP digi (filtered). Channels with less than 20 entries are not considered. Channel names of the hot cells are available in (Top) / Ecal / Errors / HotCells.'}])