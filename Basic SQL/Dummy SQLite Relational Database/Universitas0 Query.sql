-- Create Entity Tables
CREATE TABLE IF NOT EXISTS prodi (
    Nama_Prodi VARCHAR(50) NOT NULL,
    Kode_Prodi VARCHAR(20) PRIMARY KEY NOT NULL,
    Total_Kredit INTEGER NOT NULL,
    Tahun_Prodi INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS matkul (
    Nama_Matkul VARCHAR(50) NOT NULL,
    Kode_Matkul VARCHAR(20) PRIMARY KEY NOT NULL,
    Kredit_Matkul INTEGER NOT NULL,
    Tahun_Matkul INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS mahasiswa (
    Nama_Mhs VARCHAR(50) NOT NULL,
    NPM VARCHAR(20) PRIMARY KEY NOT NULL,
    Tanggal_Lahir DATE NOT NULL,
    Tahun_Masuk INTEGER NOT NULL,
    Kode_Prodi_Mhs VARCHAR(20) NOT NULL,
    FOREIGN KEY(Kode_Prodi_Mhs) REFERENCES prodi(Kode_Prodi)
);

-- Create Relationship Tables
CREATE TABLE IF NOT EXISTS milik (
    Tahun_Milik INTEGER NOT NULL,
    Semester_Milik VARCHAR(10) NOT NULL,
    Kode_Prodi_Milik VARCHAR(20) NOT NULL,
    Kode_Matkul_Milik VARCHAR (20) NOT NULL,
    FOREIGN KEY (Kode_Prodi_Milik) REFERENCES prodi(Kode_Prodi)
    FOREIGN KEY (Kode_Matkul_Milik) REFERENCES matkul(Kode_Matkul)
);

CREATE TABLE IF NOT EXISTS ambil (
    Tahun_Ambil INTEGER NOT NULL,
    Semester_Ambil VARCHAR(10) NOT NULL,
    NPM_Ambil VARCHAR(20) NOT NULL,
    Kode_Matkul_Ambil VARCHAR(20) NOT NULL,
    FOREIGN KEY (NPM_Ambil) REFERENCES mahasiswa(NPM)
    FOREIGN KEY (Kode_Matkul_Ambil) REFERENCES matkul(Kode_Matkul)
);

CREATE TABLE IF NOT EXISTS selesai (
    NPM_Selesai VARCHAR(20) NOT NULL,
    Kode_Matkul_Selesai VARCHAR(20) NOT NULL,
    Nilai_Angka REAL,
    Nilai_Huruf VARCHAR(5),
    FOREIGN KEY (NPM_Selesai) REFERENCES mahasiswa(NPM),
    FOREIGN KEY (Kode_Matkul_Selesai) REFERENCES matkul(Kode_Matkul),
    CHECK (Nilai_Angka BETWEEN 0 AND 100)
);

-- Insert Values
INSERT INTO prodi VALUES
('S1 Matematika', '44201', 144, 1961),
('S1 Statistika', '49201', 144, 2015),
('S1 Aktuaria', '94203', 144, 2017);

INSERT INTO matkul VALUES
('Geometri', 'SCMA603141', 4, 2012),
('MPKT B', 'UIGE600002', 6, 2016),
('Matematika Dasar I', 'UIST601110', 2, 2016),
('Logika dan Himpunan', 'SCMA601100', 3, 2016),
('Analisis Regresi 1', 'SCST603010', 3, 2016),
('Teori Mikroekonomi', 'SCAK603010', 3, 2017);

INSERT INTO mahasiswa VALUES
('Fawwaz Fakhrurrozi Hadiputra', '1606831602', 1998-06-22, 2016, '44201'),
('Ganeswara Pramudita', '1606835046', 1999-06-06, 2016, '44201'),
('Abyoso Hapsoro Nurhadi', '1606884136', 1998-10-22, 2016, '44201'),
('Natasha Rosaline', '1606889793', 1997-10-23, 2016, '44201'),
('Gebrina Riski Barus', '1606902662', 1998-09-26, 2016, '44201'),
('Andreas', '1706047214', 2001-03-14, 2017, '49201'),
('Adinda', '1706984985', 1999-12-02, 2017, '49201'),
('Kelvin', '1806133912', 1995-03-27, 2018, '94203'),
('Habib', '1806133982', 2000-01-01, 2018, '94203'),
('Swadesi', '1806208586', 2000-11-23, 2018, '94203');

INSERT INTO milik VALUES
(2016, 'Ganjil', '44201', 'UIST601110'),
(2017, 'Genap', '44201', 'SCMA603141'),
(2018, 'Ganjil', '44201', 'UIGE600002'),
(2018, 'Ganjil', '49201', 'UIGE600002'),
(2018, 'Ganjil', '94203', 'UIGE600002'),
(2018, 'Ganjil', '44201', 'UIST601110'),
(2018, 'Ganjil', '49201', 'UIST601110'),
(2018, 'Ganjil', '94203', 'UIST601110'),
(2018, 'Ganjil', '44201', 'SCMA601100'),
(2018, 'Ganjil', '49201', 'SCMA601100'),
(2018, 'Ganjil', '94203', 'SCMA601100'),
(2018, 'Ganjil', '49201', 'SCST603010'),
(2018, 'Ganjil', '94203', 'SCAK603010');

INSERT INTO ambil VALUES
(2016, 'Ganjil', '1606831602', 'UIGE600002'),
(2016, 'Ganjil', '1606835046', 'UIGE600002'),
(2016, 'Ganjil', '1606835046', 'SCMA601100'),
(2016, 'Ganjil', '1606889793', 'UIST601110'),
(2017, 'Genap', '1606884136', 'SCST603010'),
(2018, 'Ganjil', '1606831602', 'SCAK603010'),
(2018, 'Ganjil', '1606884136', 'SCAK603010'),
(2018, 'Ganjil', '1606889793', 'SCMA603141'),
(2018, 'Ganjil', '1606902662', 'SCMA603141'),
(2018, 'Ganjil', '1606902662', 'SCAK603010');

INSERT INTO selesai(NPM_Selesai, Kode_Matkul_Selesai, Nilai_Angka) VALUES
('1606831602', 'SCMA601100', 89),
('1606835046', 'UIGE600002', 87),
('1606884136', 'UIGE600002', 77.05),
('1606889793', 'UIST601110', 85);

-- Assign Nilai_Huruf on selesai table
UPDATE selesai
SET Nilai_Huruf = CASE
    WHEN Nilai_Angka BETWEEN 85 AND 100 THEN 'A'
    WHEN Nilai_Angka BETWEEN 80 AND 85 THEN 'A-'
    WHEN Nilai_Angka BETWEEN 75 AND 80 THEN 'B+'
    WHEN Nilai_Angka BETWEEN 70 AND 75 THEN 'B'
    WHEN Nilai_Angka BETWEEN 65 AND 70 THEN 'B-'
    WHEN Nilai_Angka BETWEEN 60 AND 65 THEN 'C+'
    WHEN Nilai_Angka BETWEEN 55 AND 60 THEN 'C'
    WHEN Nilai_Angka BETWEEN 40 AND 55 THEN 'D'
    ELSE 'E'
    END;