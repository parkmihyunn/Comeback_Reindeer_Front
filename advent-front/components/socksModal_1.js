import React, { useState, useEffect } from 'react'
import { useRef } from "react";
import Image from 'next/image';
import { Modal, Link } from "@nextui-org/react";
import AWS from "aws-sdk"
import axios from 'axios';

const SOCK_NUM = 1;

const SocksModal_1 = ({ isVisible, onClose, nickname, usertoken }) => {
	
	/*
	=== 양말 모달 동작 로직 정리 ===
	1. usertoken으로 백엔드에 get(post)요청 - usertoken, SOCK_NUM을 주고 URL과 WISHNAME을 받아와 STATE에 저장한다. 
			input value는 언제나 WISHNAME
			1) O -> 이미지 src로 URL
			2) X -> 이미지 src가 null임을 판별하고 아래부분 렌더링 시킴
							<div className="absolute text-[#791818] top-[36%]">
								<h1 className="font-medium text-[40px]">+</h1>
							</div>
	2. 미리보기 업로드
	3. 저장하기 버튼 클릭시 s3 버킷에 이미지 업로드 / 백엔드에 이미지 url, name, SOCK_NUM post 해주기
	*/

	/* AWS 설정 객체 업데이트 */
  AWS.config.update({
    region: "ap-northeast-2", // 버킷이 존재하는 리전
    credentials: new AWS.CognitoIdentityCredentials({
      IdentityPoolId: process.env.NEXT_PUBLIC__AWS_CONFIG, // cognito 인증 풀에서 받아온 키
    }),
  })

	/* 클라이언트 단에서 임시로 저장시켜서 띄워줄 부분 */
	const [imageSrc, setImageSrc] = useState('');
	const [giftName, setGiftName] = useState('');
	const [t_file, setT_file] = useState();
  const imageInput = useRef();  // input place

	const onCickImageUpload = () => {
    imageInput.current.click();
  };
  const encodeFileToBase64 = (fileBlob) => {
    console.log(fileBlob);
    console.log(fileBlob.name)
		setT_file(fileBlob)
    const reader = new FileReader();
    reader.readAsDataURL(fileBlob);
    return new Promise((resolve) => {
      reader.onload = () => {
        setImageSrc(reader.result);
        resolve();
      };}
    );
  };

  /* 이미지 가져오고 업로드 하는 핸들러 button 눌렸을때 실행할 것 */
  const handleFileInput = (fileBlob) => {
		// 파일 등록 O
    if(fileBlob !== null){
      const file = fileBlob
			const t_filetype = file.type
      const t_filename = usertoken + file.name
			const t_fileURL = "https://advent-reindeer-test.s3.ap-northeast-2.amazonaws.com/"+t_filename;
			const upload = new AWS.S3.ManagedUpload({
				params: {
					Bucket: "advent-reindeer-test",
					Key: t_filename,
					Body: file,
					ContentType: t_filetype,
				},
			})
			const promise = upload.promise()
			promise.then(
				function (data) {
					/* 백엔드에 t_filename, jwt, giftName, sock_number(=1) 넘겨주기*/
					let res = axios.post(BASE_URL+"socks/",
					{
						jwt:usertoken,
						name:giftName,
						url:t_fileURL,
						num:SOCK_NUM,
					});
					console.log(les.data)
					onClose()
					alert("이미지 업로드에 성공했습니다.")
				},
				function (err) {
					return alert(err.message)
				}
			)
    }
		// 파일 등록 X
		else { 
			return onClose() 
		}	
  }

	if(!isVisible) return null;

    return (
			<div>
			<Modal css={{background:"transparent",}} noPadding open={isVisible} onClose={onClose} width={335} height={624} animated={false}>
				<div className="inset-0 bg-opacity-75 flex justify-center items-center z-0 overflow-scroll bg-cover bg-scroll h-[684px] w-[335px]">
					<div className="socks_back">
						<div className="socks_back2">
							<div className="socks_flower">
								<Image src='/img/ornaments/6.png' width='100' height='100'></Image>
							</div>
							<button className="text-white absolute flex top-[2%] right-[6%] text-[20px]" onClick={()=>onClose()}>x</button>
							<div className="pt-[70px] h-[20px] w-[300px] top-[10%] text-white text-center text-[18px]">{nickname}님의 소원양말 1</div>
							<div className="socks_center">
								<div id="none_box_1" className="socks_edit_noneBox">
									<div className="absolute text-[#791818] top-[36%]">
										<h1 className="font-medium text-[40px]">+</h1>
									</div>
									{imageSrc && <img src={imageSrc} alt="preview-img"/>}
								</div>	
								<div id="upload" className="absolute top-[113%] w-[62px] h-[21px] flex bg-[#FF929D] justify-center z-0 rounded-full"
										onClick={ ()=> {onCickImageUpload()}}
								>
									<input type="file" onChange = {(e)=>{encodeFileToBase64(e.target.files[0])}}
												ref={imageInput} style={{ display: "none" }}
									/>
									<div className="absolute text-white top-[16%]">
										<div className="font-bold text-[11px]">사진등록</div>
									</div>
								</div>
								<div className="socks_img">
										<Image src='/img/sock_1.png' width='89' height='109.5'></Image>
								</div>
							</div>
							<div id="input-place" className="absolute top-[78%]">
								<input type="text" className="h-[38px] w-[260px] border-4 bg-[#8F1717] placeholder:text-white text-white py-5 px-4 rounded-lg" 
											value={giftName} placeholder="입력해주세요." maxlength="16"
											onChange={(e) => setGiftName(e.target.value)}
								/>
							</div>
							<div className="flex absolute bg-black w-[200px] h-[35px] top-[90%] justify-center z-0 rounded-xl">
								<button className="socks_edit_closeWord" onClick={()=>handleFileInput(t_file)}>저장하기</button>
							</div>
						  <div className="absolute w-[56px] h-[58px] top-[89%] left-[14%]">
							  <Image src='/img/closeBtn_Santa.png' width='46' height='48'/>
						  </div>
						</div>
					</div>
				</div>
			</Modal>
			</div>
    );
}
export default SocksModal_1