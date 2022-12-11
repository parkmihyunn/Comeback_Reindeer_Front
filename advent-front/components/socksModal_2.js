import React, { useState, useEffect } from 'react'
import Image from 'next/image';
import { Modal, Link } from "@nextui-org/react";

const SocksModal_2 = ({ isVisible, onClose, user, usertoken }) => {

    if(!isVisible) return null;

    return (
        <div>
        <Modal css={{background:"transparent",}} noPadding open={isVisible} onClose={onClose} width={335} height={624} animated={false}>
            <div className="inset-0 bg-opacity-75 
                            flex justify-center items-center z-0
                            overflow-scroll bg-cover bg-scroll
                            h-[684px] w-[335px]">
                <div className="socks_back">
                    <div className="socks_back2">
                        <div className="socks_flower">
                            <Image src='/img/ornaments/6.png' width='100' height='100'></Image>
                        </div>
                        <button className="x-btn text-lg" onClick={()=>onClose()}>✕</button>
                        <div className="socks_head">{}님의 소원양말 2</div>
                        <div className="socks_center2">
                            <div className="socks_giftImg">
                                <Image src='/img/nintendo.png' width='243' height='214' className="rounded-3xl"></Image>
                            </div>
                            <div className="socks_img2">
                                <Image src='/img/sock_2.png' width='89' height='109.5'></Image>
                            </div>
                        </div>
                        {/* <div className="socks_eyeNview">
                            <div className="socks_eye">
                                <Image src='/img/eye.png' width='24' height='24'></Image>
                            </div>
                            <div className="socks_view">617</div>
                        </div> */}
                        <div className="socks_giftName">닌텐도 스위치 라이트</div>
                        <div className="socks_closeBtn">
                            <button className="socks_closeWord" onClick={()=>onClose()}>닫기</button>
                        </div>
                    </div>
                </div>
            </div>
        </Modal>
        </div>
    )
}

export default SocksModal_2