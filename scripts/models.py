from sqlalchemy import Column, Float, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class XdrData(Base):
    __tablename__ = 'xdr_data'
    
    bearer_id = Column('Bearer Id',Float , primary_key=True)
    start = Column('Start', String)
    start_ms = Column('Start ms', Float)
    end = Column('End', String)
    end_ms = Column('End ms', Float)
    duration_ms = Column('Dur. (ms)', Float)
    imsi = Column('IMSI', Float)
    msisdn_number = Column('MSISDN/Number', Float)
    imei = Column('IMEI', Float)
    last_location_name = Column('Last Location Name', String)
    avg_rtt_dl_ms = Column('Avg RTT DL (ms)', Float)
    avg_rtt_ul_ms = Column('Avg RTT UL (ms)', Float)
    avg_bearer_tp_dl_kbps = Column('Avg Bearer TP DL (kbps)', Float)
    avg_bearer_tp_ul_kbps = Column('Avg Bearer TP UL (kbps)', Float)
    tcp_dl_retrans_vol_bytes = Column('TCP DL Retrans. Vol (Bytes)', Float)
    tcp_ul_retrans_vol_bytes = Column('TCP UL Retrans. Vol (Bytes)', Float)
    dl_tp_less_50_kbps_pct = Column('DL TP < 50 Kbps (%)', Float)
    dl_tp_50_to_250_kbps_pct = Column('50 Kbps < DL TP < 250 Kbps (%)', Float)
    dl_tp_250_kbps_to_1_mbps_pct = Column('250 Kbps < DL TP < 1 Mbps (%)', Float)
    dl_tp_more_than_1_mbps_pct = Column('DL TP > 1 Mbps (%)', Float)
    ul_tp_less_10_kbps_pct = Column('UL TP < 10 Kbps (%)', Float)
    ul_tp_10_to_50_kbps_pct = Column('10 Kbps < UL TP < 50 Kbps (%)', Float)
    ul_tp_50_kbps_to_300_kbps_pct = Column('50 Kbps < UL TP < 300 Kbps (%)', Float)
    ul_tp_more_than_300_kbps_pct = Column('UL TP > 300 Kbps (%)', Float)
    http_dl_bytes = Column('HTTP DL (Bytes)', Float)
    http_ul_bytes = Column('HTTP UL (Bytes)', Float)
    activity_duration_dl_ms = Column('Activity Duration DL (ms)', Float)
    activity_duration_ul_ms = Column('Activity Duration UL (ms)', Float)
    duration_ms_1 = Column('Dur. (ms).1', Float)
    handset_manufacturer = Column('Handset Manufacturer', String)
    handset_type = Column('Handset Type', String)
    nb_sec_125000b_vol_dl = Column('Nb of sec with 125000B < Vol DL', Float)
    nb_sec_1250b_to_6250b_vol_ul = Column('Nb of sec with 1250B < Vol UL < 6250B', Float)
    nb_sec_31250b_to_125000b_vol_dl = Column('Nb of sec with 31250B < Vol DL < 125000B', Float)
    nb_sec_37500b_vol_ul = Column('Nb of sec with 37500B < Vol UL', Float)
    nb_sec_6250b_to_31250b_vol_dl = Column('Nb of sec with 6250B < Vol DL < 31250B', Float)
    nb_sec_6250b_to_37500b_vol_ul = Column('Nb of sec with 6250B < Vol UL < 37500B', Float)
    nb_sec_vol_dl_less_6250b = Column('Nb of sec with Vol DL < 6250B', Float)
    nb_sec_vol_ul_less_1250b = Column('Nb of sec with Vol UL < 1250B', Float)
    social_media_dl_bytes = Column('Social Media DL (Bytes)', Float)
    social_media_ul_bytes = Column('Social Media UL (Bytes)', Float)
    google_dl_bytes = Column('Google DL (Bytes)', Float)
    google_ul_bytes = Column('Google UL (Bytes)', Float)
    email_dl_bytes = Column('Email DL (Bytes)', Float)
    email_ul_bytes = Column('Email UL (Bytes)', Float)
    youtube_dl_bytes = Column('Youtube DL (Bytes)', Float)
    youtube_ul_bytes = Column('Youtube UL (Bytes)', Float)
    netflix_dl_bytes = Column('Netflix DL (Bytes)', Float)
    netflix_ul_bytes = Column('Netflix UL (Bytes)', Float)
    gaming_dl_bytes = Column('Gaming DL (Bytes)', Float)
    gaming_ul_bytes = Column('Gaming UL (Bytes)', Float)
    other_dl_bytes = Column('Other DL (Bytes)', Float)
    other_ul_bytes = Column('Other UL (Bytes)', Float)
    total_ul_bytes = Column('Total UL (Bytes)', Float)
    total_dl_bytes = Column('Total DL (Bytes)', Float)

    def __repr__(self):
        return (
                f"start_ms={self.start_ms}, end={self.end}, end_ms={self.end_ms}, "
                f"duration_ms={self.duration_ms}, imsi={self.imsi}, msisdn_number={self.msisdn_number}, "
                f"imei={self.imei}, last_location_name={self.last_location_name}, "
                f"avg_rtt_dl_ms={self.avg_rtt_dl_ms}, avg_rtt_ul_ms={self.avg_rtt_ul_ms}, "
                f"avg_bearer_tp_dl_kbps={self.avg_bearer_tp_dl_kbps}, "
                f"avg_bearer_tp_ul_kbps={self.avg_bearer_tp_ul_kbps}, "
                f"tcp_dl_retrans_vol_bytes={self.tcp_dl_retrans_vol_bytes}, "
                f"tcp_ul_retrans_vol_bytes={self.tcp_ul_retrans_vol_bytes}, "
                f"dl_tp_less_50_kbps_pct={self.dl_tp_less_50_kbps_pct}, "
                f"dl_tp_50_to_250_kbps_pct={self.dl_tp_50_to_250_kbps_pct}, "
                f"dl_tp_250_kbps_to_1_mbps_pct={self.dl_tp_250_kbps_to_1_mbps_pct}, "
                f"dl_tp_more_than_1_mbps_pct={self.dl_tp_more_than_1_mbps_pct}, "
                f"ul_tp_less_10_kbps_pct={self.ul_tp_less_10_kbps_pct}, "
                f"ul_tp_10_to_50_kbps_pct={self.ul_tp_10_to_50_kbps_pct}, "
                f"ul_tp_50_kbps_to_300_kbps_pct={self.ul_tp_50_kbps_to_300_kbps_pct}, "
                f"ul_tp_more_than_300_kbps_pct={self.ul_tp_more_than_300_kbps_pct}, "
                f"http_dl_bytes={self.http_dl_bytes}, http_ul_bytes={self.http_ul_bytes}, "
                f"activity_duration_dl_ms={self.activity_duration_dl_ms}, "
                f"activity_duration_ul_ms={self.activity_duration_ul_ms}, "
                f"duration_ms_1={self.duration_ms_1}, "
                f"handset_manufacturer={self.handset_manufacturer}, "
                f"handset_type={self.handset_type}, "
                f"nb_sec_125000b_vol_dl={self.nb_sec_125000b_vol_dl}, "
                f"nb_sec_1250b_to_6250b_vol_ul={self.nb_sec_1250b_to_6250b_vol_ul}, "
                f"nb_sec_31250b_to_125000b_vol_dl={self.nb_sec_31250b_to_125000b_vol_dl}, "
                f"nb_sec_37500b_vol_ul={self.nb_sec_37500b_vol_ul}, "
                f"nb_sec_6250b_to_31250b_vol_dl={self.nb_sec_6250b_to_31250b_vol_dl}, "
                f"nb_sec_6250b_to_37500b_vol_ul={self.nb_sec_6250b_to_37500b_vol_ul}, "
                f"nb_sec_vol_dl_less_6250b={self.nb_sec_vol_dl_less_6250b}, "
                f"nb_sec_vol_ul_less_1250b={self.nb_sec_vol_ul_less_1250b}, "
                f"social_media_dl_bytes={self.social_media_dl_bytes}, "
                f"social_media_ul_bytes={self.social_media_ul_bytes}, "
                f"google_dl_bytes={self.google_dl_bytes}, "
                f"google_ul_bytes={self.google_ul_bytes}, "
                f"email_dl_bytes={self.email_dl_bytes}, "
                f"email_ul_bytes={self.email_ul_bytes}, "
                f"youtube_dl_bytes={self.youtube_dl_bytes}, "
                f"youtube_ul_bytes={self.youtube_ul_bytes}, "
                f"netflix_dl_bytes={self.netflix_dl_bytes}, "
                f"netflix_ul_bytes={self.netflix_ul_bytes}, "
                f"gaming_dl_bytes={self.gaming_dl_bytes}, "
                f"gaming_ul_bytes={self.gaming_ul_bytes}, "
                f"other_dl_bytes={self.other_dl_bytes}, "
                f"other_ul_bytes={self.other_ul_bytes}, "
                f"total_ul_bytes={self.total_ul_bytes}, "
                f"total_dl_bytes={self.total_dl_bytes})>")
