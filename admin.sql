insert into user (
        id,
        access_notify,
        email,
        name,
        nickname,
        password,
        profile_image,
        role,
        send_mail_check
    )
values (
        3,
        false,
        'admin@zeepy.com',
        '관리자',
        '관리자',
        '$2a$10$1XbGXbLFAYYD0VQRZDGuqOsxmu9EBhdsURmuX1JJlFahkMs.KwJcS',
        'https://zeepy.s3.ap-northeast-2.amazonaws.com/zeepyImage/dummyprofile_28pt.png',
        'ROLE_ADMIN',
        true
    );